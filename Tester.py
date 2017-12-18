'''
Created on Dec 17, 2017

@author: connerevans
'''
import unittest
from TwitterTest import screename, getTweets
from TwitterTest import api

class Test(unittest.TestCase):
    def testIfScreenNameIsRightFormat(self):
        name = 'realDonaldTrump'
        self.assertEqual(name, screename, "The names should be formatted the same")
        
    def testIfAPIWorks(self):
        self.assertIsNotNone(api, "API should not be null")

    def testIfGetTweetsIsNone(self):
        self.assertIsNotNone(getTweets('realDonaldTrump', 1, True), "Should not be null")
    
    def testIfGetTweetsSendsCorrectMessage(self):
        message = "method worked properly"
        self.assertEquals(message, getTweets('realDonaldTrump', 1, False), "Messages should be the same")
     
    
    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()