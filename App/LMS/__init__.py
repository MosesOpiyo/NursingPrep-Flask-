from flask import Blueprint

lms = Blueprint('lms',__name__)

from .Modules import views
from .TestBanks import views