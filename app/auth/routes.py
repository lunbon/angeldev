from flask import render_template
from flask import redirect, url_for
from flask import flash
from flask_login import current_user, login_user, logout_user, login_required
from .models import User
from .forms import LoginForm
from . import auth
from .decorators import moder_required


@auth.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(name=form.name.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('auth.login'))
		login_user(user, remember=True)
		return redirect(url_for('index'))
	return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))