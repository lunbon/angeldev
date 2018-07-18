from .. import db
from datetime import datetime
none_image = '/media/posters/no_poster.jpg'

class Post(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	header = db.Column(db.String(), index=True)
	body = db.Column(db.Text())
	pub_date = db.Column(db.DateTime, nullable=False,
		default=datetime.utcnow, index=True)
	path_to_image = db.Column(db.String(), default=none_image)
	url_for_image = db.Column(db.String(), default=none_image)
	def get_poster(self):
		if self.path_to_image == none_image:return self.url_for_image
		else:return self.path_to_image