from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules
from wtforms_sqlalchemy.fields import QuerySelectMultipleField,QuerySelectField

from .models import *

class PlanAdmin(ModelView):
    form_columns = ['subscription_duration','price','module','ideal_audience','saving']

class BillingAdminView(ModelView):
    # Control which columns are displayed
    form_columns = ['id', 'address', 'city', 'country', 'state', 'payment_method', 'coupon_code', 'plans', 'user', 'subscription_start_date', 'subscription_end_date']

    def get_plans_choices():
        return Plan.query

    
    form_extra_fields = {
        'plans': QuerySelectMultipleField(
            'plan',
            query_factory=get_plans_choices,
            get_label='module'
        )
    }

    form_create_rules = [
        'address', 'city', 'country', 'state', 'payment_method', 'coupon_code', 'user', 'subscription_start_date', 'subscription_end_date',
        rules.FieldSet(('plans',), 'Plaon'),
    ]

    form_edit_rules = form_create_rules