from flask import Blueprint

titles = Blueprint('titles', __name__,
					template_folder='templates')

from . import models, routes