from flask import Blueprint

lms = Blueprint('lms',__name__)

from . import views