from scripts.handlers import handler

from scripts.models.user import User

class UserPage(handler.Handler):

    def get(self, user_name):
        
        user = User.get_by_name(user_name)
        if not user:
            self.error(404)

        if self.get_current_user():
            self.render_user_page(user)
        else:
            self.redirect("/signup")
        

    def render_user_page(self, user):
        self.render("user.html", user=user, rankings=user.rankings)
