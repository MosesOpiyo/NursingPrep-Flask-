from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules
from wtforms_sqlalchemy.fields import QuerySelectMultipleField,QuerySelectField

from .models import *

class PlanAdmin(ModelView):
    form_columns = ['subscription_duration','price','ideal_audience','saving']

class BillingAdminView(ModelView):
    # Control which columns are displayed
    form_columns = ['id', 'address', 'city', 'country', 'state', 'payment_method', 'coupon_code', 'plan', 'user', 'subscription_start_date', 'subscription_end_date']