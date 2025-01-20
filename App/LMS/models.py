from App import db
from sqlalchemy import desc

course_inclusion = db.Table('course_inclusion',
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True),
    db.Column('inclusion_id', db.Integer, db.ForeignKey('inclusion.id'), primary_key=True)
)

course_module = db.Table('course_module',
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True),
    db.Column('module_id', db.Integer, db.ForeignKey('module.id'), primary_key=True)
)

module_topics = db.Table('module_topics',
    db.Column('module_id', db.Integer, db.ForeignKey('module.id'), primary_key=True),
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'), primary_key=True)
)

topic_lessons = db.Table('topic_lessons',
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'), primary_key=True),
    db.Column('lesson_id', db.Integer, db.ForeignKey('lesson.id'), primary_key=True)
)

topic_quizzes = db.Table('topic_quizzes',
    db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'), primary_key=True),
    db.Column('quiz_id', db.Integer, db.ForeignKey('quiz.id'), primary_key=True)
)

quiz_questions = db.Table('quiz_questions',
    db.Column('quiz_id', db.Integer, db.ForeignKey('quiz.id'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True)
)

question_choices = db.Table('question_choices',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True),
    db.Column('choice_id', db.Integer, db.ForeignKey('choice.id'), primary_key=True)
)

lesson_importances = db.Table('lesson_importances',
    db.Column('lesson_id', db.Integer, db.ForeignKey('lesson.id'), primary_key=True),
    db.Column('importance_id', db.Integer, db.ForeignKey('importance.id'), primary_key=True)
)

lesson_goals = db.Table('lesson_goals',
    db.Column('lesson_id', db.Integer, db.ForeignKey('lesson.id'), primary_key=True),
    db.Column('goal_id', db.Integer, db.ForeignKey('goal.id'), primary_key=True)
)

lesson_vocabulary = db.Table('lesson_vocabulary',
    db.Column('lesson_id', db.Integer, db.ForeignKey('lesson.id'), primary_key=True),
    db.Column('vocabulary_id', db.Integer, db.ForeignKey('vocabulary.id'), primary_key=True)
)

lesson_points = db.Table('lesson_points',
    db.Column('lesson_id', db.Integer, db.ForeignKey('lesson.id'), primary_key=True),
    db.Column('point_id', db.Integer, db.ForeignKey('point.id'), primary_key=True)
)

point_additionals = db.Table('point_additionals',
    db.Column('point_id', db.Integer, db.ForeignKey('point.id'), primary_key=True),
    db.Column('additional_id', db.Integer, db.ForeignKey('additional.id'), primary_key=True)
)

lesson_contents = db.Table('lesson_contents',
    db.Column('lesson_id', db.Integer, db.ForeignKey('lesson.id'), primary_key=True),
    db.Column('lessoncontent_id', db.Integer, db.ForeignKey('lessoncontent.id'), primary_key=True)
)

content_material = db.Table('content_material',
    db.Column('lessoncontent_id', db.Integer, db.ForeignKey('lessoncontent.id'), primary_key=True),
    db.Column('material_id', db.Integer, db.ForeignKey('material.id'), primary_key=True)
)

lesson_problems = db.Table('lesson_problems',
    db.Column('lesson_id', db.Integer, db.ForeignKey('lesson.id'), primary_key=True),
    db.Column('problem_id', db.Integer, db.ForeignKey('problem.id'), primary_key=True)
)

class Course(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    type = db.Column(db.String(255),nullable=False) 
    course_name = db.Column(db.String(255),nullable=False,index=True)
    introduction_message = db.Column(db.Text,nullable=False)
    details = db.Column(db.Text,nullable=False)
    inclusions = db.relationship('Inclusion', secondary=course_inclusion, backref='course')
    modules = db.relationship('Module', secondary=course_module, backref='course')

class Inclusion(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    inclusion = db.Column(db.Text,nullable=False)

class Module(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    module_name = db.Column(db.String(255),nullable=False,index=True)
    topics = db.relationship('Topic', secondary=module_topics, backref='module')

class Topic(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    topic_name = db.Column(db.String(255),nullable=False,index=True)
    lessons = db.relationship('Lesson', secondary=topic_lessons, backref='topic')
    quizzes = db.relationship('Quiz', secondary=topic_quizzes, backref='topic')

class Lesson(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    lesson_name = db.Column(db.String(255),nullable=False,index=True)
    introduction = db.Column(db.Text,nullable=False)
    importances = db.relationship('Importance', secondary=lesson_importances, backref='lesson')
    goals = db.relationship('Goal', secondary=lesson_goals, backref='lesson')
    vocabulary = db.relationship('Vocabulary', secondary=lesson_vocabulary, backref='lesson')
    points = db.relationship('Point', secondary=lesson_points, backref='lesson')
    lesson_content = db.relationship('LessonContent', secondary=lesson_contents, backref='lesson')
    practice_problems = db.relationship('Problem', secondary=lesson_problems, backref='lesson')

class Importance(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    importance = db.Column(db.Text,nullable=False)

class Goal(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    goal = db.Column(db.Text,nullable=False)

class Vocabulary(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    vocabulary = db.Column(db.Text,nullable=False)
    explaination = db.Column(db.Text,nullable=False)

class Point(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    point = db.Column(db.Text,nullable=False)
    explaination = db.Column(db.Text,nullable=False)
    additional_points = db.relationship('Additional', secondary=point_additionals, backref='point')

class Additional(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    additional_point = db.Column(db.Text,nullable=False)

class LessonContent(db.Model):
    __tablename__ = 'lessoncontent'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.Text,nullable=False)
    content = db.relationship('Material', secondary=content_material, backref='lessoncontent')

class Material(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    material = db.Column(db.Text,nullable=False)

class Problem(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    question = db.Column(db.Text,nullable=False)
    explaination = db.Column(db.Text,nullable=False)
    answer = db.Column(db.Text,nullable=False)

class Quiz(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    quiz_name = db.Column(db.String(255),nullable=False,index=True)
    quiz_details = db.Column(db.Text,nullable=False)
    questions = db.relationship('Question', secondary=quiz_questions, backref='quiz')

class Question(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    question = db.Column(db.Text,nullable=False)

    answer_id = db.Column(db.Integer, db.ForeignKey('choice.id'))
    answer = db.relationship('Choice', uselist=False, foreign_keys=[answer_id])

    explaination = db.Column(db.Text,nullable=False)
  
    choices = db.relationship('Choice', secondary=question_choices, backref='questions')

class Tag(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    tag = db.Column(db.Text,nullable=False)

class Choice(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    choice = db.Column(db.Text,nullable=False)
    rationale = db.Column(db.Text,nullable=False)


import datetime

courses_progress = db.Table('courses_progress',
    db.Column('userprogress_id', db.Integer, db.ForeignKey('userprogress.id'), primary_key=True),
    db.Column('courseprogress_id', db.Integer, db.ForeignKey('courseprogress.id'), primary_key=True)
)

modules_progress = db.Table('modules_progress',
    db.Column('courseprogress_id', db.Integer, db.ForeignKey('courseprogress.id'), primary_key=True),
    db.Column('moduleprogress_id', db.Integer, db.ForeignKey('moduleprogress.id'), primary_key=True)
)

topics_progress = db.Table('topics_progress',
    db.Column('moduleprogress_id', db.Integer, db.ForeignKey('moduleprogress.id'), primary_key=True),
    db.Column('topicprogress_id', db.Integer, db.ForeignKey('topicprogress.id'), primary_key=True)
)

lessons_progress = db.Table('lessons_progress',
    db.Column('topicprogress_id', db.Integer, db.ForeignKey('topicprogress.id'), primary_key=True),
    db.Column('lessonprogress_id', db.Integer, db.ForeignKey('lessonprogress.id'), primary_key=True)
)

quiz_evaluations = db.Table('quiz_evaluations',
    db.Column('userprogress_id', db.Integer, db.ForeignKey('userprogress.id'), primary_key=True),
    db.Column('evaluation_id', db.Integer, db.ForeignKey('evaluation.id'), primary_key=True)
)

question_markings = db.Table('question_markings',
    db.Column('evaluation_id', db.Integer, db.ForeignKey('evaluation.id'), primary_key=True),
    db.Column('marking_id', db.Integer, db.ForeignKey('marking.id'), primary_key=True)
)

class UserProgress(db.Model):
    __tablename__ = 'userprogress'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_progression = db.relationship('CourseProgress', secondary=courses_progress, backref='userprogress')
    quizzes_evaluation = db.relationship('Evaluation', secondary=quiz_evaluations, backref='userprogress')

class CourseProgress(db.Model):
    __tablename__ = 'courseprogress'
    id = db.Column(db.Integer,primary_key = True)
    course_name = db.Column(db.String(255),nullable=False,index=True)
    is_complete = db.Column(db.Boolean,default=False)
    module_progression = db.relationship('ModuleProgress', secondary=modules_progress, backref='courseprogress')

class ModuleProgress(db.Model):
    __tablename__ = 'moduleprogress'
    id = db.Column(db.Integer,primary_key = True)
    module_name = db.Column(db.String(255),nullable=False,index=True)
    is_complete = db.Column(db.Boolean,default=False)
    topics_progression = db.relationship('TopicProgress', secondary=topics_progress, backref='moduleprogress')

class TopicProgress(db.Model):
    __tablename__ = 'topicprogress'
    id = db.Column(db.Integer,primary_key = True)
    topic_name = db.Column(db.String(255),nullable=False,index=True)
    is_complete = db.Column(db.Boolean,default=False)
    lessons_progression = db.relationship('LessonProgress', secondary=lessons_progress, backref='topicprogress')

class LessonProgress(db.Model):
    __tablename__ = 'lessonprogress'
    id = db.Column(db.Integer,primary_key = True)
    lesson_name = db.Column(db.String(255),nullable=False,index=True)
    is_complete = db.Column(db.Boolean,default=False)

class Evaluation(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    quiz_name = db.Column(db.String(255),nullable=False)
    score = db.Column(db.String(255),nullable=True)
    date = db.Column(db.DateTime)
    question_marking = db.relationship('Marking', secondary=question_markings, backref='evaluation')

    def quiz_comparison(quiz_name):
        quizzes = Evaluation.query.filter_by(quiz_name=quiz_name).order_by(desc(Evaluation.date)).limit(2).all()
        return quizzes

class Marking(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    question = db.Column(db.Text,nullable=False)
    correct_answer = db.Column(db.Text,nullable=False)
    student_answer = db.Column(db.Text,nullable=False)

