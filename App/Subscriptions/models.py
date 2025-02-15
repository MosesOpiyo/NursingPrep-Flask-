from App import db
from sqlalchemy import Enum
from datetime import datetime, timezone
from ..User.models import User

subscription_module_plans = db.Table('subscription_module_plans',
    db.Column('billing_id', db.Integer, db.ForeignKey('billing.id'), primary_key=True),
    db.Column('plan_id', db.Integer, db.ForeignKey('plan.id'), primary_key=True)
)


class Billing(db.Model):
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    subscription_start_date = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    subscription_end_date = db.Column(db.DateTime)
    address = db.Column(db.Text,nullable=False)
    city = db.Column(db.String(255),nullable=False,index=True)
    country = db.Column(db.String(255),nullable=False,index=True)
    state = db.Column(db.String(255),nullable=False,index=True)
    payment_method = db.Column(Enum('PayPal', 'Credit Card', name='payment_method_enum'), nullable=False, index=True)
    coupon_code = db.Column(db.String(255),nullable=False,index=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True, default=None)
    user = db.relationship('User', backref=db.backref('billing', lazy=True))

    plans = db.relationship(
        'PLan',
        secondary=subscription_module_plans,
        backref='billing'
    )


class Plan(db.Model):
    __tablename__ = 'plan'

    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    subscription_duration = db.Column(db.String(255),nullable=False,index=True)
    module = db.Column(db.String(255),nullable=False)
    price = db.Column(db.Float)
    ideal_audience = db.Column(db.Text,nullable=False)
    saving = db.Column(db.Integer)