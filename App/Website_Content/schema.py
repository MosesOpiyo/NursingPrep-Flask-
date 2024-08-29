from App import mm,db
from flask_restful import reqparse
from flask import request
from marshmallow import fields

from .models import Page,Section,Asset,Content

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

class GetAssetSchema(mm.Schema):
    class Meta:
        model = Asset
        fields = ['title','type','asset']

class GetContentSchema(mm.Schema):
    class Meta:
        model = Content
        fields = ['title','type','content']

class GetSectionSchema(mm.Schema):
    assets = fields.Nested(GetAssetSchema,many=True) 
    content_blocks = fields.Nested(GetContentSchema,many=True)

    class Meta:
        model = Section
        fields = ['id','title','assets','content_blocks']

class GetPageSchema(mm.Schema):
    sections = fields.Nested(GetSectionSchema,many=True)

    class Meta:
        model = Page
        fields = ['id','title','slug','sections']


