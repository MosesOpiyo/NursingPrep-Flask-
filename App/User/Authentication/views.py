from flask import request,jsonify
from flask_restful import reqparse
from App import db,user_registered
from ...User import user
from ..models import User
from ...authentication import user_authentication
from ...Subscriptions.models import Plan, Billing

from google.oauth2 import id_token
from google.auth.transport import requests
from datetime import timezone,datetime

# from ...Subscriptions.models import Subscription

user_parser = reqparse.RequestParser()
user_parser.add_argument('email', type=str, required=True, help='Email is required')
user_parser.add_argument('password', type=str, required=True, help='Password is required')
user_parser.add_argument('name', type=str, required=True, help='Name is required')

login_parser = reqparse.RequestParser()
login_parser.add_argument('email', type=str, required=True, help='Email is required')
login_parser.add_argument('password', type=str, required=True, help='Password is required')

billing_parse = reqparse.RequestParser()
billing_parse.add_argument('duration', type=str, required=True, help='Duration is required')
billing_parse.add_argument('address', type=str, required=True, help='Address is required')
billing_parse.add_argument('city', type=str, required=True, help='City is required')
billing_parse.add_argument('country', type=str, required=True, help='Country is required')
billing_parse.add_argument('couponCode', type=str, required=False)
billing_parse.add_argument('paymentMethod', type=str, required=True, help='Payment Method is required')
billing_parse.add_argument('state', type=str, required=True, help='State is required')
billing_parse.add_argument('zip', type=str, required=True, help='Zip is required')


@user.route('/Authentication/TEAS/Registration',methods=['POST'])
def registration():
    data = {}
    args = user_parser.parse_args()
    username = args['name']
    email = args['email']
    password = args['password']

    billing_args = billing_parse.parse_args()
    address = billing_args['address']
    city = billing_args['city']
    country = billing_args['country']
    couponCode = billing_args['couponCode']
    paymentMethod = billing_args['paymentMethod']
    state = billing_args['state']
    zip = billing_args['zip']
    
    if billing_args['duration'] == "monthly":
        plan = Plan.query.filter_by(
            
            subscription_duration = "1 Month"
            ).first()
    else:
        plan = Plan.query.filter_by(subscription_duration = "3 Months").first()


    user_exist_email = User.query.filter_by(email = email).first()
    if user_exist_email:
       data = f"message: Email already exists."
       print(data)
       return jsonify(data),500
    
    new_user = User(
        username=username,
        email=email,
        password=password,
        plan_id=plan.id,
        billing_id=billing.id,
        
        )
    
    db.session.add(new_user)
    db.session.commit()

    billing = Billing(
        subscription_start_date=datetime.now(timezone.utc),
        address=address,
        city=city,
        country=country,
        state=state,
        payment_method = paymentMethod,
        coupon_code = couponCode,
        user_id = new_user.id,
        plan_id = plan.id
    )
    db.session.add(billing)
    db.session.commit()

    user_registered.send('user', user=user)
    user_email_check, status_code = user_authentication(email,password)
    data = user_email_check
    return jsonify(data),status_code  

@user.route('/Authentication/Login',methods=['POST'])
def login():
    data = {}
    args = login_parser.parse_args()
    email = args['email']
    password = args['password']
    
    user_email_check, status_code = user_authentication(email,password)
    if status_code == 400:
        print()
        data = jsonify({"message": "Incorrect password"})
        return data,400
    elif status_code == None:
        data = jsonify({"message": "Unregistered user"})
        return data,404
    data = jsonify(user_email_check)
    return data,200 

@user.route('/Authentication/GoogleSignIn',methods=['POST'])
def google_login():
    token = request.json['token']
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), 'YOUR_GOOGLE_CLIENT_ID')
        user_id = idinfo['sub']
        email = idinfo['email']
        username = idinfo['name']
        password=idinfo['sub'].encode()
        user_exist_email = User.query.filter_by(email = email).first()
        if user_exist_email:
            user_email_check, status_code = user_authentication(email,password)
            data = user_email_check
            return jsonify(data),status_code
        new_user = User(username=username,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        user_registered.send('user', user=user)
        user_email_check, status_code = user_authentication(email,password)
        data = user_email_check
        return jsonify(data),status_code
    except ValueError:
        return jsonify({"error": "Invalid token"}), 400