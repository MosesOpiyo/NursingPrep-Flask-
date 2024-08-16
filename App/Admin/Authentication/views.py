from flask import request,jsonify
from flask_restful import reqparse
from App import db
from ...Admin import admin_user

account_parser = reqparse.RequestParser()
account_parser.add_argument('email', type=str, required=True, help='Email is required')
account_parser.add_argument('password', type=str, required=True, help='Password is required')

@admin_user.route('/Authentication/Login',methods=['POST'])
def login():
    data = {}
    args = account_parser.parse_args()
    email = args['email']
    password = args['password']
    
    from ...authentication import admin_authentication
    user_email_check, status_code = admin_authentication(email,password)
    if status_code == 400:
        return jsonify({"message": "Incorrect password"}), 400
    elif status_code == 404:
        return jsonify({"message": "Unregistered employee"}), 404
    
    return jsonify(user_email_check), 200 