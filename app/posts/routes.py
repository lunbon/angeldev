from . import posts
from app.posts.models import Post
from flask import render_template

@posts.route('/<id>')
def get_post(id:int):
	post=Post.query.get(id)
	return render_template('posts/post.html', post=post)