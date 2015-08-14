from google.appengine.ext import db

from scripts.models.entity import Entity

class User(Entity):
	
	name = db.StringProperty(required = True)
	password = db.StringProperty(required = True)
	email = db.StringProperty(required = True)
	avatar_url = db.URLProperty()
	registered = db.DateTimeProperty(auto_now_add = True)
	
	@staticmethod
	def get_by_email(email):
		return User.all().filter("email =", email).get()
	
	@staticmethod
	def get_by_name(name):
		return User.all().filter("name =", name).get()