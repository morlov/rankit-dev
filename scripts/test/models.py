import unittest

from google.appengine.ext import testbed

from scripts.models.user import User
from scripts.models.item import Item
from scripts.models.ranking import Vote
from scripts.models.ranking import Ranking

from scripts.forms.ranking_form import RankingForm

class Test(unittest.TestCase):


    def setUp(self):
        
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()


    def tearDown(self):
        self.testbed.deactivate()

        
    def testUser(self):
        name = "test"
        email ="test@mail.ru"
        user = User(name=name, email=email, password="123")
        user.put()
        self.assertEqual(user.key(), User.get_by_name(name).key())
        self.assertEqual(user.key(), User.get_by_email(email).key())
        
        
    def testItem(self):
        name = "test"
        email ="test@mail.ru"
        user = User(name=name, email=email, password="123")
        user.put()
        
        Item(user=user, name="item1", content="content1").put()
        Item(user=user, name="item2", content="content2").put()
        
        self.assertEqual(len(Item.all().fetch(10)), 2)
        self.assertEqual(len(user.items.fetch(10)), 2)
        
        
    def testCreateRanking(self):
        name = "test"
        email ="test@mail.ru"
        user = User(name=name, email=email, password="123")
        user.put()
        
        ranking_json = '{"title": "ranking", "itemNames": ["item1", "item2", "item3"], "itemContents": ["content1", "content2", "content3"], "ranks": [0, 1, 2]}'
        ranking_form = RankingForm(ranking_json) 
        ranking = Ranking.create(user, ranking_form)
        
        votes = user.rankings.fetch(10)
        self.assertEqual(len(votes), 1)
        self.assertListEqual(ranking.get_ranks(), [[0, 1, 2]])
        
        items = ranking.get_items()
        self.assertEqual(len(items), 3)
        
        self.assertTrue(ranking.is_sorted_by(user), "Ranking should be sorted by user")
        
        
    def testUpdateRanking(self):
        user1 = User(name="test1", email="test1@mail.ru", password="123")
        user1.put()
        
        user2 = User(name="test2", email="test2@mail.ru", password="456")
        user2.put()
        
        user3 = User(name="test3", email="test3@mail.ru", password="789")
        user3.put()
        
        ranking_json = '{"title": "ranking", "itemNames": ["item1", "item2", "item3"], "itemContents": ["content1", "content2", "content3"], "ranks": [0, 1, 2]}'
        ranking_form = RankingForm(ranking_json) 
        ranking = Ranking.create(user1, ranking_form)
        self.assertEqual(ranking.number_of_votes, 1)
        
        vote2 = Vote(parent=ranking, user=user2, ranks=[2,1,0])
        vote2.put()
        ranking.update(vote2)
        self.assertEqual(ranking.number_of_votes, 2)
        
        vote3 = Vote(parent=ranking, user=user3, ranks=[2,1,0])
        vote3.put()
        ranking.update(vote3)
        self.assertEqual(ranking.number_of_votes, 3)
        
        self.assertListEqual(ranking.get_ranks(), [[0, 1, 2], [2, 1, 0], [2, 1, 0]])
        self.assertListEqual(ranking.ranks, [2, 1, 0])
        self.assertEqual(ranking.user, user1)
        self.assertListEqual([user.key() for user in ranking.get_users()], [user.key() for user in User.all()])
        
        self.assertTrue(ranking.is_sorted_by(user1), "Ranking should be sorted by user")
        self.assertTrue(ranking.is_sorted_by(user2), "Ranking should be sorted by user")
        self.assertTrue(ranking.is_sorted_by(user3), "Ranking should be sorted by user")
        
    def testLike(self):
        user = User(name="test1", email="test1@mail.ru", password="123")
        user.put()
        
        ranking_json = '{"title": "ranking", "itemNames": ["item1", "item2", "item3"], "itemContents": ["content1", "content2", "content3"], "ranks": [0, 1, 2]}'
        ranking_form = RankingForm(ranking_json) 
        ranking = Ranking.create(user, ranking_form)
        
        self.assertEqual(ranking.number_of_likes, 0)
        ranking.like(user)
        self.assertEqual(ranking.number_of_likes, 1)
        ranking.like(user)
        self.assertEqual(ranking.number_of_likes, 0)
        
        
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()