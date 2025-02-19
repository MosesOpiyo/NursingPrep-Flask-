from App import mm,db
from flask_restful import reqparse
from flask import request
from marshmallow import fields

from .models import Page,Section,Asset,Content,Pricing,Option,Feature,Benefits,Benefit

class PageSchema(mm.Schema):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title',type=str,required=True,help='Title is required')
        self.parser.add_argument('slug',type=str,required=True,help='Slug is required')

    def parse_args(self):
        return self.parser.parse_args()
    
    def new(self,data):
        title = data['title'],
        slug = data['slug'],
        page = Page(title=title,slug=slug)
        db.session.add(page)
        db.session.commit()

class AssetSchema(mm.Schema):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title',type=str,required=True,help='Title is required')

    def parse_args(self):
        return self.parser.parse_args()
    
    def new(self,data):
        title = data['title'],
        Asset = Asset(title=title)
        db.session.add(Asset)
        db.session.commit()

class AssetSchema(mm.Schema):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title',type=str,required=True,help='Title is required')
        self.parser.add_argument('type',type=str,required=True,help='Type is required')
        self.parser.add_argument('asset',type=str,required=True,help='Asset is required')

    def parse_args(self):
        return self.parser.parse_args()
    
    def new(self,data):
        title = data['title'],
        type = data['type'],
        asset = data['asset'],
        asset_model = Asset(title=title,type=type,asset=asset)
        db.session.add(asset_model)
        db.session.commit()

class ContentSchema(mm.Schema):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title',type=str,required=True,help='Title is required')
        self.parser.add_argument('type',type=str,required=True,help='Type is required')
        self.parser.add_argument('content',type=str,required=True,help='Content is required')

    def parse_args(self):
        return self.parser.parse_args()
    
    def new(self,data):
        title = data['title'],
        type = data['type'],
        content = data['content'],
        content_model = Content(title=title,type=type,content=content)
        db.session.add(content_model)
        db.session.commit()

class PricingSchema(mm.Schema):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('title',type=str,required=True,help='Title is required')
        self.parser.add_argument('content',type=str,required=True,help='Content is required')

    def parse_args(self):
        return self.parser.parse_args()
    
    def new(self,data):
        title = data['title'],
        content = data['content'],
        pricing = Pricing(title=title,content=content)
        db.session.add(pricing)
        db.session.commit()

class OptionSchema(mm.Schema):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('subscription_duration',type=str,required=True,help='Subscription Duration is required')
        self.parser.add_argument('price',type=str,required=True,help='Price is required')
        self.parser.add_argument('ideal_audience',type=str,required=True,help='Ideal Audience is required')
        self.parser.add_argument('action',type=str,required=True,help='Action is required')

    def parse_args(self):
        return self.parser.parse_args()
    
    def new(self,data):
        subscription_duration = data['subscription_duration'],
        price = data['price'],
        ideal_audience = data['ideal_audience'],
        action = data['action'],
        option = Option(subscription_duration=subscription_duration,price=price,ideal_audience=ideal_audience,action=action)
        db.session.add(option)
        db.session.commit()

class FeatureSchema(mm.Schema):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('feature',type=str,required=True,help='Feature is required')

    def parse_args(self):
        return self.parser.parse_args()
    
    def new(self,data):
        feature = data['feature'],
        
        feature = Feature(feature=feature)
        db.session.add(feature)
        db.session.commit()

class GetAssetSchema(mm.Schema):
    class Meta:
        model = Asset
        fields = ['id','title','type','class_name','asset_content','asset']

class GetContentSchema(mm.Schema):
    class Meta:
        model = Content
        fields = ['id','title','type','class_name','content']

class GetSectionSchema(mm.Schema):
    assets = fields.Nested(GetAssetSchema,many=True) 
    content_blocks = fields.Nested(GetContentSchema,many=True)

    class Meta:
        model = Section
        fields = ['id','name','section_text','title','assets','content_blocks']

class GetPageSchema(mm.Schema):
    sections = fields.Nested(GetSectionSchema,many=True)
    class Meta:
        model = Page
        fields = ['id','title','slug','sections']

class GetFeatureSchema(mm.Schema):
    class Meta:
        model = Feature
        fields = ['feature']

class GetOptionSchema(mm.Schema):
    features = fields.Nested(GetFeatureSchema,many=True)
    class Meta:
        model = Option
        fields = ['subscription_duration','price','ideal_audience','class_name','saving','action','features']

class GetPricingSchema(mm.Schema):
    options = fields.Nested(GetOptionSchema,many=True)
    class Meta:
        model = Pricing
        fields = ['title','content','options']

class GetBenefitSchema(mm.Schema):
    class Meta:
        model = Benefit
        fields = ['type','comparison','benefit','class_name','top_class_name']

class GetBenefitsSchema(mm.Schema):
    benefit_listing = fields.Nested(GetBenefitSchema,many=True)
    class Meta:
        model = Benefits
        fields = ['title','content','benefit_listing']

class GetWholePageSchema(mm.Schema):
    sections = fields.Nested(GetSectionSchema,many=True)
    pricing_items = fields.Nested(GetPricingSchema,many=True)
    benefits = fields.Nested(GetBenefitsSchema,many=True)
    class Meta:
        model = Page
        include_relationships = True
        load_instance = True
        fields = ['id','title','slug','sections','pricing_items','benefits']



