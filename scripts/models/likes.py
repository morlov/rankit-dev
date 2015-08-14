from google.appengine.ext import db
from scripts.models.user import User
from scripts.models.ranking import Ranking
from scripts.models.entity import Entity

class Like(Entity):
    user = db.ReferenceProperty(User)
    ranking = db.ReferenceProperty(Ranking)
    time = db.DateTimeProperty(auto_now_add = True)
    
