from App import db,mm
from flask_restful import reqparse

from .models import Plan,PlanEntry

class PlanSchema(mm.Schema):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('subscription_duration',type=str,required=True,help='Subscription Duration is required')
        self.parser.add_argument('module',type=str,required=True,help='Module is required')
        self.parser.add_argument('price',type=str,required=True,help='Price is required')
        self.parser.add_argument('ideal_audience',type=str,required=True,help='Ideal Audience is required')
        self.parser.add_argument('saving',type=str,required=True,help='Saving is required')

    def parse_args(self):
        return self.parser.parse_args()
    
    def new(self,data):
        duration = data['subscription_duration'],
        module = data['module'],
        price = data['price'],
        ideal_audience = data['ideal_audience'],
        saving = data['saving'],
        option = Plan(
            duration=duration,
            module=module,
            price=price,
            ideal_audience=ideal_audience,
            saving=saving
            )
        db.session.add(option)
        db.session.commit()

class PlanEntrySchema(mm.Schema):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('subscription_duration',type=str,required=True,help='Subscription Duration is required')
        self.parser.add_argument('module',type=str,required=True,help='Module is required')
        self.parser.add_argument('price',type=str,required=True,help='Price is required')
        self.parser.add_argument('ideal_audience',type=str,required=True,help='Ideal Audience is required')
        self.parser.add_argument('saving',type=str,required=True,help='Saving is required')

    def parse_args(self):
        return self.parser.parse_args()
    
    def new(self,data):
        duration = data['subscription_duration'],
        module = data['module'],
        price = data['price'],
        ideal_audience = data['ideal_audience'],
        saving = data['saving'],
        option = PlanEntry(
            duration=duration,
            module=module,
            price=price,
            ideal_audience=ideal_audience,
            saving=saving
            )
        db.session.add(option)
        db.session.commit()