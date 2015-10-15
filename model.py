#! /usr/bin/python
# -*- coding: utf-8 -*-

class Model:
    def __init__(self):
        self.loadVocabulary()
        self.getLettersCallback = None


    def loadVocabulary(self):
        self.vocabulary = Utils()
        self.vocabulary.openFile()

    def set_getLettersCB(self):
        if self.getLettersCallback:
            self.set_getLettersCB()

    def getLetters(self, gotLetters = 'абракадабра'):       # get and check letters. Check will realize later
        self.gotLetters = gotLetters
        print self.gotLetters

    def set_xxx(self, x):
        self.letters = x
        print 'xxx = ', self.letters


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


