from scripts.handlers import handler
from scripts.models.ranking import Ranking
from scripts.forms.ranking_form import RankingForm

import time

class NewRanking(handler.Handler):

    def get(self):
        user = self.get_current_user()
        if user:
            self.render("new.html", current_user=user)
        else:
            self.redirect("/signup")
      
    def post(self):
        user = self.get_current_user()
        print self.request.get('ranking')
        ranking_form = RankingForm(self.request.get('ranking')) 
        ranking = Ranking.create(user, ranking_form)
        time.sleep(0.2)
        self.redirect("/ranking/" + str(ranking.get_id()))