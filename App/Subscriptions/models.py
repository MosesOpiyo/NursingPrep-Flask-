from App import db
from sqlalchemy import Enum
from datetime import datetime, timezone
from ..User.models import User

subscription_module_plans = db.Table('subscription_module_plans',
    db.Column('billing_id', db.Integer, db.ForeignKey('billing.id'), primary_key=True),
    db.Column('planentry_id', db.Integer, db.ForeignKey('planentry.id'), primary_key=True)
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
        'PlanEntry',
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

class PlanEntry(db.Model):
    __tablename__ = 'planentry'

    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    subscription_duration = db.Column(db.String(255),nullable=False,index=True)
    module = db.Column(db.String(255),nullable=False)
    price = db.Column(db.Float)
    ideal_audience = db.Column(db.Text,nullable=False)
    saving = db.Column(db.Integer)

    def new_entry(entry,user):
        billing = Billing.query.filter_by(user=user).first()
        if billing:
            try:
                plan_entry = PlanEntry.query.filter_by(
                    module=entry.module,
                    subscription_duration=entry.subscription_duration
                ).first()
                if plan_entry:
                    if plan_entry not in billing.plans:
                        billing.plans.append(plan_entry)
                        db.session.commit()
                        return 200
                    return 200
                else:
                    # If the plan doesn't exist, create a new one
                    new_plan = PlanEntry(
                        subscription_duration=entry.subscription_duration,
                        module=entry.module,
                        price=entry.price,
                        ideal_audience=entry.ideal_audience,
                        saving=entry.saving
                    )
                    # Add to session before appending to billing
                    db.session.add(new_plan)
                    billing.plans.append(new_plan)
                    db.session.commit()
                    return 200
            
            except Exception as e:
                db.session.rollback()
                return 500