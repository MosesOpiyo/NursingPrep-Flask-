from flask import request,jsonify
from flask_restful import reqparse
from App import db
from ...User import user
from ..models import User
from ...authentication import user_authentication

user_parser = reqparse.RequestParser()
user_parser.add_argument('email', type=str, required=True, help='Email is required')
user_parser.add_argument('password', type=str, required=True, help='Password is required')


@user.route('/Authentication/Registration',methods=['POST'])
def registration():
    data = {}
    args = user_parser.parse_args()
    email = args['email']
    password = args['password']
    if '@' in email:
        username = email.split('@')[0]
    user_exist_username = User.query.filter_by(username = username).first()
    if user_exist_username:
       data = f"message: Username already exists."
       return jsonify(data),400
    user_exist_email = User.query.filter_by(email = args['email']).first()
    if user_exist_email:
       data = f"message: Email already exists."
       return jsonify(data),400
    new_user = User(username=username,email=email,password=password)
    db.session.add(new_user)
    db.session.commit()
    user_email_check, status_code = user_authentication(email,password)
    data = user_email_check
    return jsonify(data),status_code  

@user.route('/Authentication/Login',methods=['POST'])
def login():
    data = {}
    args = user_parser.parse_args()
    email = args['email']
    password = args['password']
    
    from ...authentication import admin_authentication
    user_email_check, status_code = admin_authentication(email,password)
    if status_code == 400:
        data = jsonify({"message": "Incorrect password"})
        return data,400
    elif status_code == 404:
        data = jsonify({"message": "Unregistered employee"})
        return data,404
    data = jsonify(user_email_check)
    return data,200 