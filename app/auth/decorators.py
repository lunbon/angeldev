from flask import redirect, url_for
from flask_login import current_user, login_required

def moder_required(view):
	def warpper():
		if current_user.moder:
			view()
		else:
			redirect(url_for('index'))
	return warpper