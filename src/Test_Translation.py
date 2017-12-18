'''
Created on Dec 17, 2017

@author: connorfairman
'''
import unittest
from Secret import consumer_key, access_token, consumer_secret,\
    access_token_secret
from translation_practice import tweetTranslation, screenname, language,\
    translateTextFile

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
  
# Test to make sure screenname is not NULL
# Passes
    def test_Screenname(self):
        self.assertIsNotNone(screenname, msg=None)
         
# Test to make sure language is Spanish
# Passes
    def test_Langauge(self):
        self.assertIs(language, 'es')

# Test to confirm that the translateTextFile function has no return value
# Passes
    def test_translateTextFile(self):
        result = translateTextFile("source-tweet.txt", 'es', "translation.txt")
        self.assertIsNone(result)
    
# Test to confirm that tweetTranslation function has no return value
# Passes
    def test_tweetTranslation(self):
        result = tweetTranslation("translation.txt")
        self.assertIsNone(result)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()