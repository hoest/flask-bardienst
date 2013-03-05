from bardienst import app, models, db, forms, lm
from flask import g, session, render_template, redirect, url_for, flash, request, send_from_directory
from flask.ext.login import login_required, logout_user, login_user
from werkzeug import secure_filename


@app.before_request
def check_user_status():
  """
  Check global user_id
  """
  g.user = None
  if "user_id" in session:
    g.user = models.User.query.get(session["user_id"])


@lm.user_loader
def load_user(user_id):
  """
  LoginManager method
  """
  return models.User.query.get(user_id)


@app.route("/")
# @login_required
def welcome():
  """
  Shows all available diaries, includes a form to create a new one.
  """
  return "Welcome!"

