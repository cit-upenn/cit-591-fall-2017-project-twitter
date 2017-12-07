'''
Created on Nov 28, 2017

@author: connorfairman
'''
from googletrans import Translator
from PyQt4 import QtCore

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

