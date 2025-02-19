from . import content
from flask import jsonify

from .models import Page
from .schema import GetPageSchema,GetWholePageSchema

@content.route('/pages/<string:slug>',methods=['GET'])
def getPageContent(slug):
    data = {}
    page_schema = GetPageSchema()
    second_page_schema = GetWholePageSchema()
    page_data = Page.query.filter_by(slug=slug).first()
    if page_data:
        if page_data.pricing_items or page_data.benefits:
            page = second_page_schema.dump(page_data)
        else:
            page = page_schema.dump(page_data)
        data = page,200
    else:
        data = jsonify('Page not found'),404
    return data
    


