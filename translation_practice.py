'''
Created on Nov 28, 2017

@author: connorfairman
'''

from googletrans import Translator

translator = Translator()
translation = translator.translate("We are gonna win so big that we are going to get bored with winning", 'es', 'en')
print(translation.text)

file_object = open("translation.txt", "w")
file_object.truncate(0)
file_object.write(translation.text)
file_object.close()

