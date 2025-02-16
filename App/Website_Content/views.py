from . import content
from flask import jsonify

from .models import Page
from .schema import GetPageSchema

@content.route('/Page-Content/<string:page>',methods=['GET'])
def getPageContent(page):
    data = {}
    page_schema = GetPageSchema()
    page_data = Page.query.filter_by(name = 'Homepage').first()
    if page_data:
        page = page_schema.dump(page_data)
        data = page,200
    else:
        data = jsonify('Page not found'),404
    return data
    


