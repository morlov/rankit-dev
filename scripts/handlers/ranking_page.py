from scripts.handlers import handler
import json

from scripts.models.ranking import Ranking
from scripts.models.ranking import Vote

class RankingPage(handler.Handler):

    def get(self, ranking_id):
        ranking = Ranking.get_by_id(int(ranking_id))
        if not ranking:
            self.error(404)
            return

        user = self.get_current_user()
        if user:
            is_sorted = ranking.is_sorted_by(user)
            self.render("ranking.html", user=ranking.user, ranking=ranking, is_sorted=is_sorted, current_user=user)
        else:
            self.redirect("/signup")
      
    def post(self, ranking_id):
        
        user = self.get_current_user()
        ranking = Ranking.get_by_id(int(ranking_id))

        if user in ranking.get_users():
            self.response.out.write('You have already submitted this ranking!')
            return

        ranking_json = json.loads(self.request.get('ranking'))
        vote = Vote(user=user, parent=ranking, ranks=ranking_json["ranks"])
        vote.put()
        ranking.update(vote)
        self.redirect('/ranking/'+str(ranking_id))