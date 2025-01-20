from App import db
from sqlalchemy import Enum

class Plan(db.Model):
    __tablename__ = 'plan'

    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    subscription_duration = db.Column(db.String(255),nullable=False,index=True)
    price = db.Column(db.Float)
    ideal_audience = db.Column(db.Text,nullable=False)
    saving = db.Column(db.Integer)


class Billing(db.Model):
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    address = db.Column(db.Text,nullable=False)
    city = db.Column(db.String(255),nullable=False,index=True)
    country = db.Column(db.String(255),nullable=False,index=True)
    state = db.Column(db.String(255),nullable=False,index=True)
    payment_method = db.Column(Enum('PayPal', 'Credit Card', name='payment_method_enum'), nullable=False, index=True)
    coupon_code = db.Column(db.String(255),nullable=False,index=True)