import os

class Config(object):
	 SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	 SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/mac/projects/angel_dev/app.db'
	 SQLALCHEMY_TRACK_MODIFICATIONS = False