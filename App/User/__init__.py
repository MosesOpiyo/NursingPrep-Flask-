from flask import Blueprint

user = Blueprint('user',__name__)

from .Authentication import views
from .Profile import views