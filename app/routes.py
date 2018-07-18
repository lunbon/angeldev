from . import app
from app.posts.models import Post
from flask import render_template

@app.route('/')
def index():
	posts = Post.query.order_by(Post.pub_date.desc()).all()
	return render_template('index.html', posts=posts)
@app.route('/FAQ')
def get_faq():
	faq=Post.query.filter_by(header="FAQ").first_or_404()
	return render_template('faq.html', faq=faq)