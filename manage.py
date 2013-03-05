#!/usr/bin/env python
from flask.ext.script import Manager, Shell, Server, prompt_bool
from bardienst import app, db, models

manager = Manager(app)

manager.add_command("runserver", Server())
manager.add_command("shell", Shell())


@manager.command
def drop():
  "Drops database tables"
  if prompt_bool("Are you sure you want to lose all your data"):
    db.drop_all()


@manager.command
def create():
  "Creates database tables from sqlalchemy models"
  db.create_all()
  populate()


@manager.command
def recreate():
  "Recreates database tables (same as issuing 'drop' and then 'create')"
  drop()
  create()


@manager.command
def populate():
  "Populate database with default data"
  u = models.User('Jelle', 'jelle@hoest.nl', '0628062912', '123')
  db.session.add(u)
  db.session.commit()

  s = models.Schedule()
  s.user_id = u.id
  s.thursday = 1
  s.saterday = 1
  db.session.add(s)
  db.session.commit()

manager.run()
