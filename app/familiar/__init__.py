from flask import Blueprint

familiar_blueprint = Blueprint('familiar', __name__, template_folder="templates/familiar")

from . import views