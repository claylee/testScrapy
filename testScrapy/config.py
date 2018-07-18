# configuration

class Config(object):
	DATABASE = 'tmp/flaskr.db'
	DEBUG = True
	SECRET_KEY = 'development key'
	USERNAME = 'admin'
	PASSWORD = 'default'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/flaskr.db'
