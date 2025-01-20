from App import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime, timezone

from ..Subscriptions.models import Plan,Billing

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),nullable=False,index=True)
    email = db.Column(db.String(255),nullable=True,index=True)
    pass_secure = db.Column(db.String(255))

    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=False, default=None)
    plan = db.relationship('Plan', backref=db.backref('user', lazy=True))

    billing_id = db.Column(db.Integer, db.ForeignKey('billing.id'), nullable=False, default=None)
    billing = db.relationship('Billing', backref=db.backref('user', lazy=True))
    subscription_start_date = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    subscription_end_date = db.Column(db.DateTime)

    __table_args__ = (
        db.UniqueConstraint('username', name='unique_username_constraint'),
        db.UniqueConstraint('email', name='unique_email_constraint'),
    )
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'Account {self.username}'