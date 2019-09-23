from flask import Blueprint

mn = Blueprint("main", __name__)

from App.views import main