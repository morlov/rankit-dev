import webapp2

import scripts.handlers.login
import scripts.handlers.new_ranking
import scripts.handlers.user_page
import scripts.handlers.ranking_page
import scripts.handlers.main_page

app = webapp2.WSGIApplication([
    ('/', scripts.handlers.main_page.MainPage),
    ('/new', scripts.handlers.new_ranking.NewRanking),
    ('/ranking/([0-9]+)', scripts.handlers.ranking_page.RankingPage),
    ('/user/([a-zA-Z0-9_-]+)', scripts.handlers.user_page.UserPage),
    ('/signup', scripts.handlers.login.Signup),
    ('/signin', scripts.handlers.login.Signin),
    ('/signout', scripts.handlers.login.Signout)
    ], debug=True)


