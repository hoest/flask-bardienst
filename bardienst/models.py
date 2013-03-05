from bardienst import db, bcrypt
from flask.ext.login import UserMixin
from datetime import datetime


ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model, UserMixin):
  """
  User object
  """
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(1024), nullable=False)
  email = db.Column(db.String(1024), nullable=False)
  phone = db.Column(db.String(256), nullable=False)
  password = db.Column(db.String(1024), nullable=False)
  role = db.Column(db.SmallInteger, default=ROLE_USER)
  created = db.Column(db.DateTime, default=datetime.now)

  def __init__(self, name, email, phone, password):
    self.name = name
    self.email = email
    self.phone = phone
    self.password = bcrypt.generate_password_hash(password)

  def is_password_correct(self, password):
    return bcrypt.check_password_hash(self.password, password)

  def get_schedule(self):
    return Schedule.query.filter(Schedule.user_id == self.id).first()

  def can_work(self, type, date):
    dow = date.weekday()
    schedule = self.get_schedule()
    can_type = type == schedule.type or schedule.type == TYPE_ALL
    can_dow = False

    if dow == 0:
      can_dow = schedule.monday == 1
    elif dow == 1:
      can_dow = schedule.tuesday == 1
    elif dow == 2:
      can_dow = schedule.wednesday == 1
    elif dow == 3:
      can_dow = schedule.thursday == 1
    elif dow == 4:
      can_dow = schedule.friday == 1
    elif dow == 5:
      can_dow = schedule.saterday == 1
    elif dow == 6:
      can_dow = schedule.sunday == 1

    return can_type and can_dow

  def __repr__(self):
    return u"<User %s>" % (self.email)


TYPE_KITCHEN = 0
TYPE_BAR = 1
TYPE_ALL = 2


class Schedule(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
  monday = db.Column(db.SmallInteger, default=0)
  tuesday = db.Column(db.SmallInteger, default=0)
  wednesday = db.Column(db.SmallInteger, default=0)
  thursday = db.Column(db.SmallInteger, default=0)
  friday = db.Column(db.SmallInteger, default=0)
  saterday = db.Column(db.SmallInteger, default=0)
  sunday = db.Column(db.SmallInteger, default=0)
  type = db.Column(db.SmallInteger, default=TYPE_BAR)

  def __repr__(self):
    return u"<Schedule %s>" % (self.id)

