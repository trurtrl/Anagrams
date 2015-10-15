#! /usr/bin/python
# -*- coding: utf-8 -*-

class Model:
    def __init__(self):
        self.lang_changed = True
        self.newGame()

#        self.getLettersCallback = None


    def newGame(self):
        if self.lang_changed:
            self.loadFile()
#        print self.dictionary[:10]

    def loadFile(self, file_name = 'vocabulary'):
        import codecs
        self.file_temp = codecs.open(file_name)
        self.prepare()
    def prepare(self):			# Create a list with words from opened file
        self.dictionary = []
        for word in self.file_temp.readlines():
            word = word.replace('\n','').decode('UTF-8')
            self.dictionary.append(word)
        self.file_temp.close()




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


class GetWord:				# get word from widget 'ent'(Entry).From letters of this word will assemble new words.
    def __init__(self):
        pass



if __name__ == '__main__':
    mo = Model()
