'''
Created on Nov 28, 2017

@author: connorfairman
'''
from __future__ import unicode_literals
from Secret import consumer_key, consumer_secret, access_token, access_token_secret
import tweepy
from googletrans import Translator


# Provide consumer key and access token
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Define API
api = tweepy.API(auth)

# Function for getting a handle's tweets
def getTweets(name, number, rt):
    tweets = api.user_timeline(screen_name = name, count = number, include_rts = rt)
    
    for status in tweets:
        print (status.text)
        file_object = open("source-tweet.txt", "w")
        file_object.truncate(0)
        text = status.text
        correcttext = text.encode('UTF-8')
        file_object.write(correcttext)
        file_object.close()

# Function for translating text from a text file and then storing it in another text file
def translateTextFile(srcFileName, destinationLanguage, destFileName):
    file_object = open(srcFileName, "r")
    tweet = file_object.read()
    translator = Translator()
    translation = translator.translate(tweet, destinationLanguage, 'en')
    print(translation.text)
    file_object.close() 
    file_object1 = open(destFileName, "w")
    file_object1.truncate(0)
    correcttext = translation.text.encode('UTF-8')
    file_object1.write(correcttext)
    file_object1.close()

# Must input Twitter handle in between single quotes!!! (' ')    
screenname = input("Enter a user's handle: ")
getTweets(screenname, 1, True)

translateTextFile("source-tweet.txt",'es', "translation.txt")

# Use same file and put all functions in one module - done
# Combine our parts into one module to get it to run together - done
# Look up Python testing - done(ish) Still need to implement unittesting and pyCoverage
# structure code above into unique functions - done
######################################################################################

