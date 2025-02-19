from App import db,mm
from flask_restful import reqparse
from marshmallow import fields
from ..models import TestBankQuestion, QuestionChoice


class QuestionChoiceSchema(mm.Schema):
    class Meta:
        model = QuestionChoice
        fields = ["__all__"]

class TestBankQuestionSchema(mm.Schema):
    answer = fields.Nested(QuestionChoiceSchema)
    choices = fields.Nested(QuestionChoiceSchema, many=True)

    class Meta:
        model = TestBankQuestion
        fields = ["__all__"]