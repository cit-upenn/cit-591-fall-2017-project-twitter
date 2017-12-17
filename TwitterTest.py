'''
Created on Dec 15, 2017

@author: connerevans
'''
from __future__ import unicode_literals
import tweepy
from Carbon.QuickTime import kNAStuffToneDescriptionSelect
from Secret import consumer_key, consumer_secret, access_token, access_token_secret


#consumer_key = 'KMW0enDSiGQGzZEQKtBHEwGVa'
#consumer_secret = 'BP0XI3EubKSWMqFeSfc26Ygddck7cQJ7u8gd1Ixuyelw1FBlbT'
#access_token = '223724013-Ch206Es5QsoG6ST1gBycnYaanSVtjUufEDbgcJgZ'
#access_token_secret = 'DF9UMHhvpU8oCQHgGUCHxIxSW4DLB5bdm5lYSQFdVg05I'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


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

screename = input("Enter a user's handle: ")
getTweets(screename, 1, True)

