#! /usr/bin/python
# -*- coding: utf-8 -*-


class Model:
    def __init__(self):
        self.loadVocabulary()



	view = View()
	view.set_start_game_callback()



    def loadVocabulary(self):
	self.vocabulary = Utils()
	self.vocabulary.openFile()



    def searchWords(self):
	pass

    def comparison(self):		# compare entered words and founded
	pass


class Utils:
    def openFile(self, file_name = 'vocabulary'):
	import codecs
	self.file_temp = codecs.open(file_name)
	self.prepare()

    def prepare(self):			# Create list with words from opened file
	self.dictionary = []
	for word in self.file_temp.readlines():
	    word = word.replace('\n','').decode('UTF-8')
	    self.dictionary.append(word)
	self.file_temp.close()
	print self.dictionary[:10]


class GetWord:				# get word from widget 'ent'(Entry).From letters of this word will assemble new words.
    def __init__(self):
	pass

