from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_admin.contrib.sqla import ModelView
from decouple import config
from datetime import timedelta
import os

from .config import config_options


api = Api()
db = SQLAlchemy()
migrate = Migrate()
mm = Marshmallow()
admin = Admin(name='Admin', template_mode='bootstrap3')
jwt = JWTManager()
secret_key = os.urandom(24)

def create_app(config_option):
    app = Flask(__name__,instance_relative_config=True)
    basedir = os.path.abspath(os.path.dirname(__file__)) 
    app.config.from_object(config_options[config_option])
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICACTIONS'] = False
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    app.app_context().push()
    api.init_app(app)
    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    mm.init_app(app)
    admin.init_app(app)
    db.create_all()

    from App.Website_Content import content as content_blueprint
    app.register_blueprint(content_blueprint,url_prefix='/Content',name='system-content')

    from App.Admin import admin_user as admin_blueprint
    app.register_blueprint(admin_blueprint,url_prefix='/Admin',name='system-admin')
    
    from App.User import user as user_blueprint
    app.register_blueprint(user_blueprint,url_prefix='/User',name='system-user')
    
    from App.Website_Content.admin import PageAdmin
    from App.Website_Content.models import Page,Content
    admin.add_view(PageAdmin(Page, db.session))
    admin.add_view(ModelView(Content,db.session))

    return app