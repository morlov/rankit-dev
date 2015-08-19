from scripts.handlers import handler

class EditProfile(handler.Handler):

    def get(self):
        user = self.get_current_user()
        if user:
            self.render("/edit_profile.html", current_user=user)
        else:
            self.redirect("/signup")
      
    def post(self):
        print "Profile updated"
        # TODO: create profile