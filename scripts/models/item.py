from google.appengine.ext import db

from scripts.models.user import User
from scripts.models.entity import Entity

class Item(Entity):
    
    user = db.ReferenceProperty(User, collection_name="items")
    name = db.StringProperty(required = False)
    content = db.TextProperty(required = False)
    created = db.DateTimeProperty(auto_now_add = True)