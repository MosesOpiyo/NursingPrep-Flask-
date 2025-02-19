from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules
from wtforms_sqlalchemy.fields import QuerySelectMultipleField,QuerySelectField

from .models import *

class PageAdmin(ModelView):
    form_columns = ['title','slug','sections','pricing_items','benefits']

    def get_sections_choices():
        return Section.query

    def get_pricing_choices():
        return Pricing.query
    
    def get_benefits_choices():
        return Benefits.query
    
    form_extra_fields = {
        'sections': QuerySelectMultipleField(
            'Section',
            query_factory=get_sections_choices,
            get_label='name'
        ),
        'pricing_items': QuerySelectMultipleField(
            'Pricing',
            query_factory=get_pricing_choices,
            get_label='title'
        ),
        'benefits': QuerySelectMultipleField(
            'Benefits',
            query_factory=get_benefits_choices,
            get_label='title'
        )
    }

    form_create_rules = [
        'title','slug',
        rules.FieldSet(('sections',), 'Section'),
        rules.FieldSet(('pricing_items',), 'Pricing'),
        rules.FieldSet(('benefits',), 'Benefits')
    ]

    form_edit_rules = form_create_rules

class SectionAdmin(ModelView):
    form_columns = ['title','name','assets','section_text','content_blocks']

    def get_assets_choices():
        return Asset.query

    def get_content_blocks_choices():
        return Content.query
    
    form_extra_fields = {
        'assets': QuerySelectMultipleField(
            'Asset',
            query_factory=get_assets_choices,
            get_label='type'
        ),
        'content_blocks': QuerySelectMultipleField(
            'Content',
            query_factory=get_content_blocks_choices,
            get_label='type'
        )
    }


    form_create_rules = [
        'title','name','section_text',
        rules.FieldSet(('assets',), 'Asset'),
        rules.FieldSet(('content_blocks',), 'Content'),
    ]

    form_edit_rules = form_create_rules


class AssetAdmin(ModelView):
    form_columns = ['title','type','class_name','asset_content','asset']

class ContentAdmin(ModelView):
    form_columns = ['title','type','class_name','content']

class PricingAdmin(ModelView):
    form_columns = ['title','content','page_id','options']

    def get_option_choices():
        return Option.query
    
    form_extra_fields = {
        'options': QuerySelectMultipleField(
            'Option',
            query_factory=get_option_choices,
            get_label='subscription_duration'
        )
    }


    form_create_rules = [
        'title','content','page_id',
        rules.FieldSet(('options',), 'Option'),
    ]

    form_edit_rules = form_create_rules

class OptionAdmin(ModelView):
    form_columns = ['subscription_duration','price','saving','class_name','ideal_audience','action','features']

    def get_feature_choices():
        return Feature.query
    
    form_extra_fields = {
        'features': QuerySelectMultipleField(
            'Feature',
            query_factory=get_feature_choices,
            get_label='feature'
        )
    }


    form_create_rules = [
        'subscription_duration','price','ideal_audience','action','saving','class_name',
        rules.FieldSet(('features',), 'Feature'),
    ]

    form_edit_rules = form_create_rules

class FeatureAdmin(ModelView):
    form_columns = ['feature']

class BenefitsAdmin(ModelView):
    form_columns = ['title','content','page_id','benefit_listing']

    def get_benefit_choices():
        return Benefit.query
    
    form_extra_fields = {
        'benefit_listing': QuerySelectMultipleField(
            'Benefit',
            query_factory=get_benefit_choices,
            get_label='type'
        )
    }


    form_create_rules = [
        'title','content','page_id',
        rules.FieldSet(('benefit_listing',), 'Benefit'),
    ]

    form_edit_rules = form_create_rules

class BenefitAdmin(ModelView):
    form_columns = ['type','comparison','benefit','class_name','top_class_name']



