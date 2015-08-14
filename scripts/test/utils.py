
import unittest
from scripts.utils.group_choice import Rules


class Test(unittest.TestCase):


    def testBorda(self):
        ranks = [[0,1,2]]
        self.assertListEqual(Rules.borda(ranks), [0, 1, 2])
        
        ranks = [[0,1,2], [2,1,0], [2,1,0]]
        self.assertListEqual(Rules.borda(ranks), [2, 1, 0])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()