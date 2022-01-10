from flask import Blueprint

familiar_api = Blueprint('familiar_api', __name__)

from . import views