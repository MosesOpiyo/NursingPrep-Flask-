from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_admin import Admin
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_caching import Cache
from flask_admin.contrib.sqla import ModelView
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from decouple import config
from datetime import timedelta
from blinker import signal
import os
import redis

from .config import config_options



api = Api()
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
mm = Marshmallow()
admin = Admin(name='Admin', template_mode='bootstrap3')
jwt = JWTManager()
secret_key = os.urandom(24)
cache = Cache(config={'CACHE_TYPE': 'simple'})

limiter = Limiter(key_func=get_remote_address)

env_name = os.getenv("FLASK_ENV", "development")

# redis_client = redis.StrictRedis(
#         host=app.config["REDIS_HOST"],
#         port=app.config["REDIS_PORT"],
#         db=app.config["REDIS_DB"],
#         password=app.config["REDIS_PASSWORD"],
#         decode_responses=True
#     )

user_registered = signal('user-registered')

def create_app(config_option):
    app = Flask(__name__,instance_relative_config=True)
    basedir = os.path.abspath(os.path.dirname(__file__)) 
    app.config.from_object(config_options[config_option])
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_BINDS'] = {
    'backup': 'sqlite:///' + os.path.join(basedir, 'backup.db'),
    'current': 'sqlite:///' + os.path.join(basedir, 'db.sqlite'),
}
    app.config['SQLALCHEMY_TRACK_MODIFICACTIONS'] = False
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    # app.config.from_object(config_options[env_name])
    app.app_context().push()
    api.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    mm.init_app(app)
    admin.init_app(app)  # Use 'redis' or 'memcached' in production
    cache.init_app(app)
    db.create_all()


    from App.Website_Content import content as content_blueprint
    app.register_blueprint(content_blueprint,url_prefix='/Content',name='system-content')

    from App.LMS import lms as lms_blueprint
    app.register_blueprint(lms_blueprint,url_prefix='/LMS',name='system-lms')

    from App.Admin import admin_user as admin_blueprint
    app.register_blueprint(admin_blueprint,url_prefix='/Admin',name='system-admin')
    
    from App.User import user as user_blueprint
    app.register_blueprint(user_blueprint,url_prefix='/User',name='system-user')

    from App.User.admin import UserModelView
    from App.User.models import User
    
    from App.Website_Content.admin import PageAdmin,SectionAdmin,AssetAdmin,ContentAdmin,PricingAdmin,OptionAdmin,FeatureAdmin,BenefitsAdmin,BenefitAdmin
    from App.Website_Content.models import Page,Section,Asset,Content,Pricing,Option,Feature,Benefits,Benefit
    from App.Subscriptions.admin import PlanAdmin,BillingAdminView
    from App.Subscriptions.models import Plan,PlanEntry,Billing
    from App.LMS.admin import CourseAdmin,InclusionAdmin,ModuleAdmin,TopicAdmin,LessonAdmin,ImportanceAdmin,GoalAdmin,VocabularyAdmin,PointAdmin,AdditionalAdmin,LessonContentAdmin,MaterialAdmin,ProblemAdmin,QuizAdmin,QuestionAdmin,ChoiceAdmin
    from App.LMS.models import Course,Inclusion,Module,Topic,Lesson,Importance,Goal,Vocabulary,Point,Additional,LessonContent,Material,Problem,Quiz,Question,Choice

    admin.add_view(UserModelView(User, db.session))
    
    admin.add_view(PageAdmin(Page, db.session))
    admin.add_view(SectionAdmin(Section,db.session))
    admin.add_view(AssetAdmin(Asset,db.session))
    admin.add_view(ContentAdmin(Content,db.session))
    admin.add_view(PricingAdmin(Pricing,db.session))
    admin.add_view(OptionAdmin(Option,db.session))
    admin.add_view(FeatureAdmin(Feature,db.session))
    admin.add_view(BenefitsAdmin(Benefits,db.session))
    admin.add_view(BenefitAdmin(Benefit, db.session))

    admin.add_view(PlanAdmin(Plan, db.session))
    admin.add_view(PlanAdmin(PlanEntry, db.session))
    admin.add_view(BillingAdminView(Billing, db.session))

    admin.add_view(CourseAdmin(Course, db.session))
    admin.add_view(InclusionAdmin(Inclusion, db.session))
    admin.add_view(ModuleAdmin(Module, db.session))
    admin.add_view(TopicAdmin(Topic, db.session))
    admin.add_view(LessonAdmin(Lesson, db.session))
    admin.add_view(ImportanceAdmin(Importance, db.session))
    admin.add_view(GoalAdmin(Goal, db.session))
    admin.add_view(VocabularyAdmin(Vocabulary, db.session))
    admin.add_view(PointAdmin(Point, db.session))
    admin.add_view(AdditionalAdmin(Additional, db.session))
    admin.add_view(LessonContentAdmin(LessonContent, db.session))
    admin.add_view(MaterialAdmin(Material, db.session))
    admin.add_view(ProblemAdmin(Problem, db.session))
    admin.add_view(QuizAdmin(Quiz, db.session))
    admin.add_view(QuestionAdmin(Question, db.session))
    admin.add_view(ChoiceAdmin(Choice, db.session))

    from sqlalchemy.orm import sessionmaker, scoped_session
    from sqlalchemy import create_engine

    # Define paths for the current and backup databases
    basedir = os.path.abspath(os.path.dirname(__file__))
    current_db_uri = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    backup_db_uri = 'sqlite:///' + os.path.join(basedir, 'backup.db')

    # Create separate sessions for current and backup databases
    current_engine = create_engine(current_db_uri)
    backup_engine = create_engine(backup_db_uri)

    CurrentSession = scoped_session(sessionmaker(bind=current_engine))
    BackupSession = scoped_session(sessionmaker(bind=backup_engine))

    current_session = CurrentSession()
    backup_session = BackupSession()

    try:
        # Get all models defined in the app
        all_models = [Page, Section, Asset, Content, Pricing, Option, Feature, Benefits, Benefit]

        for model in all_models:
            # Check if the current database has data for the model
            if not current_session.query(model).first():
                print(f"No data found for {model.__name__} in the current database. Checking backup...")
                # Fetch all data from the backup database
                backup_data = backup_session.query(model).all()
                if backup_data:
                    print(f"Found {len(backup_data)} records for {model.__name__} in the backup database. Copying...")
                    for record in backup_data:
                        # Handle copying data carefully, including relationships
                        if isinstance(record, model):  # Make sure the record is the correct type
                            # Create a new instance of the model and manually copy over the fields
                            new_record = model()
                            for column in model.__table__.columns:
                                setattr(new_record, column.name, getattr(record, column.name))
                            
                            # Handle relationships carefully
                            if hasattr(model, 'sections'):
                                # Add related objects to the session before assigning to the new instance
                                new_sections = []
                                for section in record.sections:
                                    section_in_session = current_session.merge(section)  # Attach to current session
                                    new_sections.append(section_in_session)
                                new_record.sections = new_sections

                            if hasattr(model, 'pricing_items'):
                                new_pricing_items = []
                                for pricing in record.pricing_items:
                                    pricing_in_session = current_session.merge(pricing)  # Attach to current session
                                    new_pricing_items.append(pricing_in_session)
                                new_record.pricing_items = new_pricing_items

                            if hasattr(model, 'benefits'):
                                new_benefits = []
                                for benefit in record.benefits:
                                    benefit_in_session = current_session.merge(benefit)  # Attach to current session
                                    new_benefits.append(benefit_in_session)
                                new_record.benefits = new_benefits

                            # Add the new record to the session
                            current_session.add(new_record)

                    current_session.commit()
                    print(f"Copied {len(backup_data)} records for {model.__name__} to the current database.")
                else:
                    print(f"No data found for {model.__name__} in the backup database.")
            else:
                print(f"Data already exists for {model.__name__} in the current database.")

    except Exception as e:
        print(f"An error occurred: {e}")
        current_session.rollback()
    finally:
        # Close both sessions
        current_session.close()
        backup_session.close()
        CurrentSession.remove()
        BackupSession.remove()

    return app