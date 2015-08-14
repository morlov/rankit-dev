from google.appengine.ext import db

class Entity(db.Model):

    def get_id(self):
        return self.key().id()