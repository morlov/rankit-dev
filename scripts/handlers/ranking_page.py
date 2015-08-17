from scripts.handlers import handler
import json

from scripts.models.ranking import Ranking

class RankingPage(handler.Handler):

    def get(self, ranking_id):
        ranking = Ranking.get_by_id(int(ranking_id))
        if not ranking:
            self.error(404)
            return

        user = self.get_current_user()
        if user:
            is_sorted = ranking.is_sorted_by(user)
            self.render("ranking.html", user=user, ranking=ranking, is_sorted=is_sorted)
        else:
            self.redirect("/signup")
      
    def post(self, ranking_id):
        
        user = self.get_current_user()
        ranking = Ranking.get_by_id(int(ranking_id))

        if user in ranking.get_users():
            self.response.out.write('You have already submitted this ranking!')
            return

        item_ids = json.loads(self.request.get('ranking'))
        print item_ids
        #ranks = ranking.get_rank_by_items(item_ids)
        #print ranks
        #ranking.update(ranks, user)
        self.redirect('/ranking/'+str(ranking_id))