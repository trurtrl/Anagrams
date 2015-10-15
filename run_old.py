# -*- coding: utf-8 -*-


import Tkinter as tk

class Model:
    def __init__(self):
	pass


    def getVocabulary(self):
#	FileToDictionary.__init__(self.FileToDictionary)
	self.vocabulary = Utils()
	self.vocabulary.openFile()


    def searchWords(self):
	pass

    def comparison(self):
	pass
    def getWord(self):			# get word from widget 'ent'(Entry)
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



class View:
    def __init__(self):
	self.root = tk.Tk()
	self.root.title('-= Anagrams =-')
	self.frame1 = tk.Frame(self.root, width = 80, height = 10)
	self.frame2 = tk.Frame(self.root, width = 60, height = 50)
	self.frame3 = tk.Frame(self.root, width = 20, height = 50)

	self.but1 = tk.Button(self.frame1, text = 'Новая игра', bg = 'grey')
	self.but2 = tk.Button(self.frame1, text = 'Начать', bg = 'darkgreen')

	self.text1 =  tk.Text(self.frame2, width = 55, height = 45, bd = 3)

	self.but3  =  tk.Button(self.frame3, text = 'Проверить')


	self.mount_Widgets()

	self.root.mainloop()


    def dynamicWidgets(self):
	quit(self.lab)
	quit(self.ent)
	self.lab = tk.Label(self.frame1, text = 'Введине \n слово', font = 'Arial 14', width = 20, height = 5)
	self.ent = tk.Entry(self.frame1, width = 50, bd = 3, font = 'Arial 14')


    def mount_Widgets(self):
	self.frame1.pack()
	self.frame2.pack(side = 'left')
	self.frame3.pack(side = 'left')

	self.but1.grid(row = 0, column = 1, padx = 10)
	self.but2.grid(row = 0, column = 4, padx = 10)
	self.text1.pack()
	self.but3.pack()


    def mount_dynamicWidgets(self):



	self.lab.grid(row = 0, column = 2, padx = 10)
	self.ent.grid(row = 0, column = 3, padx = 10)
	self.ent.focus()




class Controller:
    def __init__(self):
        model = Model()
        model.getVocabulary()
	view = View()



    def changeWidgets(self):
#	self.view.
	self.model.getWord()


if __name__ == '__main__':
#    root = tk.Tk()
    app = Controller()


