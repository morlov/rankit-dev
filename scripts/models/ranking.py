from google.appengine.ext import db
from datetime import datetime

from scripts.models.item import Item
from scripts.models.user import User
from scripts.models.entity import Entity

from scripts.utils.group_choice import Rules

class Vote(Entity):  
    user = db.ReferenceProperty(User)
    created = db.DateTimeProperty(auto_now_add=True)
    ranks = db.ListProperty(int)
    
class Ranking(Entity):   
    title = db.StringProperty()
    user = db.ReferenceProperty(User, collection_name="rankings")
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty
    ranks = db.ListProperty(int)
    number_of_votes = db.IntegerProperty()
    number_of_likes = db.IntegerProperty()
    likes = db.ListProperty(db.Key)
    
    @staticmethod
    def create(user, form):     
        ranking = Ranking(user=user, title=form.title, number_of_votes=0, number_of_likes=0)
        ranking.put()
        vote = Vote(ranks=form.ranks, user=user, parent=ranking)
        vote.put()
        ranking.update(vote)
        for (name, content) in zip(form.item_names, form.item_contents):
            Item(parent=ranking, user=user, name=name, content=content).put()
        return ranking
    
    @db.transactional
    def update(self, vote):
        self.ranks = Rules.borda(self.get_ranks())
        self.updated = datetime.now()
        self.number_of_votes += 1
        self.put()
    
    @db.transactional   
    def like(self, user):
        if user.key() in self.likes:
            self.likes.remove(user.key())
            self.number_of_likes -= 1
        else:
            self.likes.append(user.key())
            self.number_of_likes += 1
        self.put()
       
    def get_ranks(self): 
        return [vote.ranks for vote in Vote.all().ancestor(self)]
    
    def get_items(self):
        return [item for item in Item.all().ancestor(self)]
    
    def get_users(self):
        return [vote.user for vote in Vote.all().ancestor(self)]
    
    def is_sorted_by(self, user):
        return user.key() in [user.key() for user in self.get_users()]
    
