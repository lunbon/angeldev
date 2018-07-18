from flask import Blueprint
from .. import login_manager

auth = Blueprint('auth',__name__,
					template_folder='templates')

from . import models, routes

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(user_id)