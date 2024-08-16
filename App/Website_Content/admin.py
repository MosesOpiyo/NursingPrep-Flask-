from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules
from wtforms_sqlalchemy.fields import QuerySelectMultipleField

from .models import Content

class PageAdmin(ModelView):
    form_columns = ['name', 'contents']

    def get_content_choices():
        return Content.query

    form_extra_fields = {
        'contents': QuerySelectMultipleField(
            'Content',
            query_factory=get_content_choices,
            get_label='section'
        )
    }

    form_create_rules = [
        'name',
        rules.FieldSet(('contents',), 'Contents')
    ]

    form_edit_rules = form_create_rules