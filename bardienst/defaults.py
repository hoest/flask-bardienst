import os

SECRET_KEY = "<SECRET_KEY>"
DEBUG = True
BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

SQLALCHEMY_DATABASE_URI = "sqlite:////{0}/db/bardienst.db".format(BASEDIR)

CSRF_ENABLED = True

LOCALE = "nl_NL"

