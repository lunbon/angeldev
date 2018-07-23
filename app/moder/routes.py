from flask import redirect, url_for, abort
from flask import render_template
from flask_login import current_user
from . import moder
from .forms import EditForm,EditChapterForm
from .. import db
from ..posts.models import Post
from ..titles.models import Title, Chapter

@moder.before_request
def before_request():
	if not current_user.is_authenticated or not current_user.moder:
		abort(404)

@moder.route('/delete_post/<id>')
def delete_post(id:int):
	post=Post.query.filter_by(id=id).first_or_404()
	db.session.delete(post)
	db.session.commit()
	return redirect(url_for('index'))

@moder.route('/create_post', methods=['GET','POST'])
def create_post():
	form=EditForm()
	if form.validate_on_submit():
		post=Post(header=form.header.data, body=form.body.data)
		if form.url.data:
			post.url_for_image=form.url.data
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('moder/edit_post.html', form=form)

@moder.route('/edit_post/<id>', methods=['GET','POST'])
def edit_post(id):
	form=EditForm()
	post=Post.query.filter_by(id=id).first_or_404()
	if form.validate_on_submit():
		post.header=form.header.data
		post.body=form.body.data
		post.url_for_image=form.url.data
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('index'))
	form.header.data=post.header
	form.body.data=post.body
	form.url.data=post.url_for_image
	return render_template('moder/edit_post.html', form=form)

@moder.route('/delete_title/<id>')
def delete_title(id:int):
	title=Title.query.filter_by(id=id).first_or_404()
	db.session.delete(title)
	db.session.commit()
	return redirect(url_for('titles.all_titles'))

@moder.route('/create_title', methods=['GET','POST'])
def create_title():
	form=EditForm()
	if form.validate_on_submit():
		title=Title(name=form.header.data, description=form.body.data)
		if form.url.data:
			title.url_for_image=form.url.data
		db.session.add(title)
		db.session.commit()
		return redirect(url_for('titles.all_titles'))
	return render_template('moder/edit_post.html', form=form)

@moder.route('/edit_title/<id>', methods=['GET','POST'])
def edit_title(id):
	form=EditForm()
	title=Title.query.filter_by(id=id).first_or_404()
	if form.validate_on_submit():
		title.name=form.header.data
		title.description=form.body.data
		title.url_for_image=form.url.data
		db.session.add(title)
		db.session.commit()
		return redirect(url_for('all_titles'))
	form.header.data=title.name
	form.body.data=title.description
	form.url.data=title.url_for_image
	return render_template('moder/edit_post.html', form=form)

@moder.route('/title/<id>/create_chapter', methods=['GET','POST'])
def create_chapter(id:int):
	form=EditChapterForm()
	if form.validate_on_submit():
		chapter=Chapter(name=form.name.data, 
			description=form.description.data,url_for_image=form.url.data)
		chapter.title = Title.query.get(id)
		chapter.number = form.number.data
		db.session.add(chapter)
		db.session.commit()
		return redirect(url_for('titles.get_title', id=id))
	return render_template('moder/edit_chapter.html', form=form)

@moder.route('/title/<id>/edit_chapter/<num>', methods=['GET','POST'])
def edit_chapter(id:int, num:int):
	form=EditChapterForm()
	title=Title.query.filter_by(id=id).first_or_404()
	chapter=Chapter.query.filter_by(number=num).first_or_404()
	if form.validate_on_submit():
		chapter.name=form.name.data
		chapter.description=form.description.data
		chapter.url_for_image=form.url.data
		chapter.number = form.number.data
		db.session.add(chapter)
		db.session.commit()
		return redirect(url_for('index'))
	form.name.data=chapter.name
	form.description.data=chapter.description
	form.url.data=chapter.url_for_image
	return render_template('moder/edit_chapter.html', form=form)