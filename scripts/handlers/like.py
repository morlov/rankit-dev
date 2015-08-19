from scripts.handlers import handler

from scripts.models.user import User
from scripts.models.ranking import Ranking

class LikeHandler(handler.Handler):

    def post(self, user_name, ranking_id): 
        
        user = User.get_by_name(user_name)
        ranking = Ranking.get_by_id(int(ranking_id))
        ranking.like(user)
        
        if not user:
            self.error(404)
        if self.get_current_user():
            self.write(str(ranking.number_of_likes))
        else:
            self.redirect("/signup")
