# from App import db,mm
# from flask_restful import reqparse

# from .models import Subscription

# class SubscriptionSchema(mm.Schema):
#     def __init__(self):
#         self.parser = reqparse.RequestParser()
#         self.parser.add_argument('duration',type=str,required=True,help='Subscription Duration is required')
#         self.parser.add_argument('price',type=str,required=True,help='Price is required')
#         self.parser.add_argument('ideal_audience',type=str,required=True,help='Ideal Audience is required')
#         self.parser.add_argument('saving',type=str,required=True,help='Saving is required')

#     def parse_args(self):
#         return self.parser.parse_args()
    
#     def new(self,data):
#         duration = data['duration'],
#         price = data['price'],
#         ideal_audience = data['ideal_audience'],
#         saving = data['saving'],
#         option = Subscription(duration=duration,price=price,ideal_audience=ideal_audience,saving=saving)
#         db.session.add(option)
#         db.session.commit()