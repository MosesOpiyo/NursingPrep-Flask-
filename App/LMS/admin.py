from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules
from wtforms_sqlalchemy.fields import QuerySelectMultipleField,QuerySelectField

from .models import *

def get_inclusions_choices():
    return Inclusion.query

def get_modules_choices():
    return Module.query

def get_topics_choices():
    return Topic.query

def get_lessons_choices():
    return Lesson.query

def get_importances_choices():
    return Importance.query

def get_goals_choices():
    return Goal.query

def get_vocabulary_choices():
    return Vocabulary.query

def get_points_choices():
    return Point.query

def get_additional_choices():
    return Additional.query

def get_content_choices():
    return LessonContent.query

def get_material_choices():
    return Material.query

def get_problem_choices():
    return Problem.query

def get_quiz_choices():
    return Quiz.query

def get_question_choices():
    return Question.query

def get_choice_choices():
    return Choice.query

# Admin interface for Course
class CourseAdmin(ModelView):
    form_columns = ['course_name', 'type', 'introduction_message', 'details', 'inclusions', 'modules']

    form_extra_fields = {
        'inclusions': QuerySelectMultipleField(
            'Inclusions',
            query_factory=get_inclusions_choices,
            get_label='inclusion'
        ),
        'modules': QuerySelectMultipleField(
            'Modules',
            query_factory=get_modules_choices,
            get_label='module_name'
        )
    }

    form_create_rules = [
        'course_name', 'type', 'introduction_message', 'details',
        rules.FieldSet(('inclusions',), 'Inclusions'),
        rules.FieldSet(('modules',), 'Modules')
    ]
    form_edit_rules = form_create_rules

# Admin interface for Inclusion
class InclusionAdmin(ModelView):
    form_columns = ['inclusion']

# Admin interface for Module
class ModuleAdmin(ModelView):
    form_columns = ['module_name', 'topics']

    form_extra_fields = {
        'topics': QuerySelectMultipleField(
            'Topics',
            query_factory=get_topics_choices,
            get_label='topic_name'
        )
    }

    form_create_rules = [
        'module_name',
        rules.FieldSet(('topics',), 'Topics')
    ]
    form_edit_rules = form_create_rules

# Admin interface for Topic
class TopicAdmin(ModelView):
    form_columns = ['topic_name', 'lessons', 'quizzes']

    form_extra_fields = {
        'lessons': QuerySelectMultipleField(
            'Lessons',
            query_factory=get_lessons_choices,
            get_label='lesson_name'
        ),
        'quizzes': QuerySelectMultipleField(
            'Quizzes',
            query_factory=get_quiz_choices,
            get_label='quiz_name'
        )
    }

    form_create_rules = [
        'topic_name',
        rules.FieldSet(('lessons',), 'Lessons'),
        rules.FieldSet(('quizzes',), 'Quizzes')
    ]
    form_edit_rules = form_create_rules

# Admin interface for Lesson
class LessonAdmin(ModelView):
    form_columns = ['lesson_name', 'introduction', 'importances', 'goals', 'vocabulary', 'points', 'lesson_content', 'practice_problems']

    form_extra_fields = {
        'importances': QuerySelectMultipleField(
            'Importance',
            query_factory=get_importances_choices,
            get_label='importance'
        ),
        'goals': QuerySelectMultipleField(
            'Goals',
            query_factory=get_goals_choices,
            get_label='goal'
        ),
        'vocabulary': QuerySelectMultipleField(
            'Vocabulary',
            query_factory=get_vocabulary_choices,
            get_label='vocabulary'
        ),
        'points': QuerySelectMultipleField(
            'Points',
            query_factory=get_points_choices,
            get_label='point'
        ),
        'lesson_content': QuerySelectMultipleField(
            'Lesson Content',
            query_factory=get_content_choices,
            get_label='title'
        ),
        'practice_problems': QuerySelectMultipleField(
            'Problems',
            query_factory=get_problem_choices,
            get_label='question'
        )
    }

    form_create_rules = [
        'lesson_name', 'introduction',
        rules.FieldSet(('importances',), 'Importance'),
        rules.FieldSet(('goals',), 'Goals'),
        rules.FieldSet(('vocabulary',), 'Vocabulary'),
        rules.FieldSet(('points',), 'Points'),
        rules.FieldSet(('lesson_content',), 'Lesson Content'),
        rules.FieldSet(('practice_problems',), 'Practice Problems')
    ]
    form_edit_rules = form_create_rules

# Admin interface for Importance
class ImportanceAdmin(ModelView):
    form_columns = ['importance']

# Admin interface for Goal
class GoalAdmin(ModelView):
    form_columns = ['goal']

# Admin interface for Vocabulary
class VocabularyAdmin(ModelView):
    form_columns = ['vocabulary', 'explaination']

# Admin interface for Point
class PointAdmin(ModelView):
    form_columns = ['point', 'explaination', 'additional_points']

    form_extra_fields = {
        'additional_points': QuerySelectMultipleField(
            'Additional Points',
            query_factory=get_additional_choices,
            get_label='additional_point'
        )
    }

    form_create_rules = [
        'point', 'explaination',
        rules.FieldSet(('additional_points',), 'Additional Points')
    ]
    form_edit_rules = form_create_rules

# Admin interface for Additional
class AdditionalAdmin(ModelView):
    form_columns = ['additional_point']

# Admin interface for LessonContent
class LessonContentAdmin(ModelView):
    form_columns = ['title', 'content']

    form_extra_fields = {
        'content': QuerySelectMultipleField(
            'Content',
            query_factory=get_material_choices,
            get_label='material'
        )
    }

    form_create_rules = [
        'title',
        rules.FieldSet(('content',), 'Content')
    ]
    form_edit_rules = form_create_rules

# Admin interface for Material
class MaterialAdmin(ModelView):
    form_columns = ['material']

# Admin interface for Problem
class ProblemAdmin(ModelView):
    form_columns = ['question', 'explaination', 'answer']

# Admin interface for Quiz
class QuizAdmin(ModelView):
    form_columns = ['quiz_name', 'quiz_details', 'questions']

    form_extra_fields = {
        'questions': QuerySelectMultipleField(
            'Questions',
            query_factory=get_question_choices,
            get_label='question'
        )
    }

    form_create_rules = [
        'quiz_name', 'quiz_details',
        rules.FieldSet(('questions',), 'Questions')
    ]
    form_edit_rules = form_create_rules

# Admin interface for Question
class QuestionAdmin(ModelView):
    form_columns = ['question', 'answer', 'choices']

    form_extra_fields = {
        'choices': QuerySelectMultipleField(
            'Choices',
            query_factory=get_choice_choices,
            get_label='choice'
        )
    }

    form_create_rules = [
        'question', 'answer',
        rules.FieldSet(('choices',), 'Choices')
    ]
    form_edit_rules = form_create_rules

# Admin interface for Choice
class ChoiceAdmin(ModelView):
    form_columns = ['choice']
    