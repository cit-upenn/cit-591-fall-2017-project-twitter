'''
Created on Nov 28, 2017

@author: connorfairman
'''
from googletrans import Translator


def translateTextFile():
    file_object = open("source-tweet.txt", "r")
    tweet = file_object.read()
    translator = Translator()
    translation = translator.translate(tweet, 'es', 'en')
    print(translation.text)
    file_object.close() 
    file_object1 = open("translation.txt", "w")
    file_object1.truncate(0)
    file_object1.write(translation.text)
    file_object1.close()

translateTextFile()


# Instead of watching a file, create a new text file every time you take in a tweet
# Combine our parts into one module to get it to run together
# Look up Python testing
# structure code above into unique functions
######################################################################################

