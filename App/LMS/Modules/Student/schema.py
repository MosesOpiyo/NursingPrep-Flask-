from App import db,mm
from flask_restful import reqparse
from marshmallow import fields
from ...models import Course, Inclusion, Module, Topic, Lesson, Importance, Goal, Vocabulary, Point, Additional, LessonContent, Material, Problem, Quiz, Question, Choice
                    

class InclusionSchema(mm.Schema):
    class Meta:
        model = Inclusion
        fields = ['inclusion']
        
class ImportanceSchema(mm.Schema):
    class Meta:
        model = Importance
        fields = ['importance']
        
class GoalSchema(mm.Schema):
    class Meta:
        model = Goal
        fields = ['goal']
        
class VocabularySchema(mm.Schema):
    class Meta:
        model = Vocabulary
        fields = ['vocabulary','explaination']
           
class AdditionalSchema(mm.Schema):
    class Meta:
        model = Additional
        fields = ['additional_point']

class PointSchema(mm.Schema):
    additional_points = fields.Nested(AdditionalSchema, many=True)

    class Meta:
        model = Point
        fields = ['point','explaination']
        
class MaterialSchema(mm.Schema):
    class Meta:
        model = Material
 
class ContentSchema(mm.Schema):
    content = fields.Nested(MaterialSchema, many=True)

    class Meta:
        model = LessonContent
        fields = ['__all__']
        
class ProblemSchema(mm.Schema):
    class Meta:
        model = Problem
        fields = ['__all__']
        
class ChoiceSchema(mm.Schema):
    class Meta:
        model = Choice
        fields = ["__all__"]

class QuestionSchema(mm.Schema):
    answer = fields.Nested(ChoiceSchema)
    choices = fields.Nested(ChoiceSchema, many=True)

    class Meta:
        model = Question
        fields = ["__all__"]

class QuizSchema(mm.Schema):
    questions = fields.Nested(QuestionSchema, many=True)

    class Meta:
        model = Quiz
        fields = ["__all__"]

class LessonSchema(mm.Schema):
    importances = fields.Nested(ImportanceSchema, many=True)
    goals = fields.Nested(GoalSchema, many=True)
    vocabulary = fields.Nested(VocabularySchema, many=True)
    points = fields.Nested(PointSchema, many=True)
    lesson_content = fields.Nested(ContentSchema, many=True)
    practice_problems = fields.Nested(ProblemSchema, many=True)

    class Meta:
        model = Lesson
        fields = ['lesson_name','introduction','importances','goals','vocabulary','points','lesson_content','practice_problems']

class TopicSchema(mm.Schema):
    lessons = fields.Nested(LessonSchema, many=True)
    quizzes = fields.Nested(QuizSchema, many=True)

    class Meta:
        model = Topic
        fields = ['topic_name','lessons','quizzes']
        
class ModuleSchema(mm.Schema):
    topics = fields.Nested(TopicSchema, many=True)
    class Meta:
        model = Module
        fields = ['module_name','topics']
        
class CourseSchema(mm.Schema):
    inclusions = fields.Nested(InclusionSchema, many=True)
    modules = fields.Nested(ModuleSchema, many=True)
    
    class Meta:
        model = Course
        fields = ['course_name','inclusions','modules']

class CourseInfoSchema(mm.Schema):
    inclusions = fields.Nested(InclusionSchema, many=True)
    modules = fields.Nested(ModuleSchema, many=True)
    class Meta:
        model = Course
        fields = ['type','course_name','introduction_message','details','inclusions','modules']
        
    
