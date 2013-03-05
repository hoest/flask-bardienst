from bardienst import defaults
from flask import Flask
from flask.ext.login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flaskext.bcrypt import Bcrypt
import locale

# create app
app = Flask(__name__)

# config
app.config.from_object(defaults)
app.config.from_envvar("bardienst.settings", silent=True)

# local
locale.setlocale(locale.LC_ALL, app.config["LOCALE"])

# SQLAlchemy
db = SQLAlchemy(app)

# Login
lm = LoginManager()
lm.setup_app(app)
lm.login_view = "login"
lm.login_message = u"U dient in te loggen."

# Bcrypt
bcrypt = Bcrypt(app)

from bardienst import views, models

