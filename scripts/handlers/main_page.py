from scripts.handlers import handler

from scripts.models.ranking import Ranking


class MainPage(handler.Handler):

    def get(self):
        if self.get_current_user():
            self.render_main_page()
        else:
            self.redirect("/signup")

    def render_main_page(self):
        user = self.get_current_user()
        rankings = Ranking.all().order('-created').fetch(limit=0, offset=10)
        self.render("main.html", current_user=user, user=user, rankings=rankings)