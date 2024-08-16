from flask import jsonify
from flask_jwt_extended import create_access_token,create_refresh_token
from datetime import datetime,timedelta
from .Admin.models import AdminUser
from .User.models import User

def admin_authentication(email,password):
    account_email_check = AdminUser.query.filter_by(email = email).first()
    if account_email_check is None:
        return None,404
    else:
        check = AdminUser.verify_password(account_email_check,password)
        if check:
            account = account_email_check.id
            access_token = create_access_token(identity=account)
            refresh_token = create_refresh_token(identity=account)
            tokens = {"access": str(access_token), "refresh": str(refresh_token)}
            return tokens,200
        else:
            return None,400

def user_authentication(email,password):
    user_email_check = User.query.filter_by(email = email).first()
    if user_email_check is not None:
        is_checked = False
        try:
            check = User.verify_password(user_email_check,password)
            if check:
                user = user_email_check.id
                access_token = create_access_token(identity=user)
                refresh_token = create_refresh_token(identity=user)
                tokens = {"access": str(access_token), "refresh": str(refresh_token)}
                return tokens,200
        except:
            return None,404
    else:
        return None,404