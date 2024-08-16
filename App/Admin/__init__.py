from flask import Blueprint

admin_user = Blueprint('admin_user',__name__)

from .Authentication import views