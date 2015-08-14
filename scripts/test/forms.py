
import unittest

from scripts.forms.ranking_form import RankingForm

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testRankingForm(self):
        ranking_json = '{"title": "ranking", "item_names": ["item1", "item2", "item3"], "item_contents": ["content1", "content2", "content3"], "ranks": [1, 2, 3]}'
        ranking_form = RankingForm(ranking_json) 
        self.assertEqual(ranking_form.title,"ranking")
        self.assertListEqual(ranking_form.item_names, ["item1", "item2", "item3"])
        self.assertListEqual(ranking_form.item_contents, ["content1", "content2", "content3"])
        self.assertListEqual(ranking_form.ranks, [1, 2, 3])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()