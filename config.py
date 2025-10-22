import os


class Config:
	SECRET_KEY = os.environ.get('FLASK_SECRET', 'dev-secret')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///seloedu.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
	DEBUG = True

