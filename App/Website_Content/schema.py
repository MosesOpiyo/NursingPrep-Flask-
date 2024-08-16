from App import mm,db
from flask_restful import reqparse
from flask import request
from marshmallow import fields

from .models import Page,Content

class ContentSchema(mm.Schema):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('section', type=str, required=True, help='Section is required')
        self.parser.add_argument('content', type=str, required=True, help='Content is required')

    def parse_args(self):
        return self.parser.parse_args()
    
    def new(self,data):
        section = data['section'],
        content = data['content'],
        content = Content(section=section,content=content)
        db.session.add(content)
        db.session.commit()

class GetContentSchema(mm.Schema):
    class Meta:
        model = Content
        fields = ['section','content']

class PageSchema(mm.Schema):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True, help='Name is required')

    def parse_args(self):
        return self.parser.parse_args()
    
    def new(self,data):
        name = data['name'],
        page = Page(name=name)
        db.session.add(page)
        db.session.commit()

class GetPageSchema(mm.Schema):
    contents = fields.List(fields.Nested(GetContentSchema))
    
    class Meta:
        model = Page
        fields = ['name','contents']


