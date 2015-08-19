import webapp2

import scripts.handlers.login
import scripts.handlers.new_ranking
import scripts.handlers.user_page
import scripts.handlers.ranking_page
import scripts.handlers.main_page
import scripts.handlers.edit_profile
import scripts.handlers.like

app = webapp2.WSGIApplication([
    ('/', scripts.handlers.main_page.MainPage),
    ('/new', scripts.handlers.new_ranking.NewRanking),
    ('/ranking/([0-9]+)', scripts.handlers.ranking_page.RankingPage),
    ('/user/([a-zA-Z0-9_-]+)', scripts.handlers.user_page.UserPage),
    ('/edit_profile', scripts.handlers.edit_profile.EditProfile),
    ('/like/([a-zA-Z0-9_-]+)/([0-9]+)', scripts.handlers.like.LikeHandler),
    ('/signup', scripts.handlers.login.Signup),
    ('/signin', scripts.handlers.login.Signin),
    ('/signout', scripts.handlers.login.Signout)
    ], debug=True)


