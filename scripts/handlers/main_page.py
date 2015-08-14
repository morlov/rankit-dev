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
        rankings = Ranking.all().order('-created').fetch(50)
        self.render("main.html", user=user, rankings=rankings)