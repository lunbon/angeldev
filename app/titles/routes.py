from flask import render_template
from flask import request
from . import titles
from app.titles.models import Title, Chapter
	
@titles.route('/')
def all_titles():
	titles = Title.query.all()	
	return render_template('titles/titles.html',
							all_titles=titles)
@titles.route('/<id>')
def get_title(id:int):
	title = Title.query.get(id)
	chapters = title.chapters
	if type(chapters)==type([]):
		chapters.sort(key=lambda c:c.id, reverse=True)
	return render_template('titles/title.html', title=title,chapters=chapters)
@titles.route('/chapter/<id>')
def get_chapter(id:int):
	chapter = Chapter.query.get(id)
	return render_template('titles/chapter.html', chapter=chapter)
