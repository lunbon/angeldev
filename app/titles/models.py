from .. import db
from ..posts.models import Post

none_image = '/media/posters/no_poster.jpg'

class Title(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String())
	path_to_image = db.Column(db.String(), 
					default=none_image)
	url_for_image = db.Column(db.String(), 
					default=none_image)
	description = db.Column(db.String())
	def get_poster(self):
		if self.path_to_image == none_image:return self.url_for_image
		else:return self.path_to_image

class Chapter(db.Model):
	def __init__(self,**kwargs):
		super(Chapter, self).__init__(**kwargs)
		post=Post(header=self.name,body=self.description, 
			url_for_image=self.url_for_image)
		db.session.add(post)
		db.session.commit()
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String())
	number = db.Column(db.Float(), index=True)
	description = db.Column(db.String())
	title_id = db.Column(db.Integer, db.ForeignKey('title.id'),
		nullable=False)
	title = db.relationship('Title',
		backref=db.backref('chapters', lazy='dynamic'))
	path_to_image = db.Column(db.String(), 
					default=none_image)
	url_for_image = db.Column(db.String(), 
					default=none_image)
	
	def get_poster(self):
		if self.path_to_image == none_image:return self.url_for_image
		else:return self.path_to_image