'''
Created on Dec 17, 2017

@author: connorfairman
'''
import unittest
from Secret import consumer_key, access_token, consumer_secret,\
    access_token_secret

class TestTranslation(unittest.TestCase):

# Test to make sure consumer_key is not NULL
# Passes
    def test_ConsumerKey(self):
        self.assertIsNotNone(consumer_key, msg=None)
    
# Test to make sure access_token is not NULL
# Passes
    def test_AccessToken(self):
        self.assertIsNotNone(access_token, msg=None)

# Test to make sure consumer_secret is not NULL
# Passes
    def test_ConsumerSecret(self):
        self.assertIsNotNone(consumer_secret, msg=None)

# Test to make sure access_token_secret is not NULL
# Passes
    def test_Access_Token_Secret(self):
        self.assertIsNotNone(access_token_secret, msg=None)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()