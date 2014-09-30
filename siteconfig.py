import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(_basedir, 'db_repository')

SECRET_KEY = "home video"
USERNAME = "admin"
PASSWORD = "default"

del os
