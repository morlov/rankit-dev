from google.appengine.ext import db
from scripts.models.user import User
from scripts.models.ranking import Ranking
from scripts.models.entity import Entity

class Comment(Entity):

    user = db.ReferenceProperty(User)
    ranking = db.ReferenceProperty(Ranking)
    text = db.TextProperty(required = True)
    time = db.DateTimeProperty(auto_now_add = True)
