from flask import jsonify
from flask_jwt_extended import create_access_token,create_refresh_token
from datetime import datetime,timedelta
from .Admin.models import AdminUser
from .User.models import User
from .Subscriptions.models import Billing,Plan,PlanEntry

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

def user_authentication(email,password,module,duration):
    user_email_check = User.query.filter_by(email = email).first()
    if user_email_check is not None:
        check = User.verify_password(user_email_check,password)
        if check:
            user_billing = Billing.query.filter_by(user = user_email_check).first()
            if user_billing is not None:
                plan_check = Plan.query.filter_by(
                    module = module,
                    subscription_duration = duration
                    ).first()
                new_entry = PlanEntry.new_entry(plan_check,user_email_check)
                if new_entry == 200:
                    if check:
                            user = user_email_check.id
                            access_token = create_access_token(identity=user)
                            refresh_token = create_refresh_token(identity=user)
                            tokens = {"access": str(access_token), "refresh": str(refresh_token)}
                            return tokens,200
        else:
            return None,400            
    else:
        return "User is None",404