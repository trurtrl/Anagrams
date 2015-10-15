# -*- coding: utf-8 -*-


import Tkinter as tk

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

###--------------------------------
#####			VIEW's part
###--------------------------------

class View:
    def __init__(self, before_start = False):
	self.before_start = before_start
	self.root = tk.Tk()
	self.root.title('-= Anagrams =-')
	self.frame1 = tk.Frame(self.root, width = 80, height = 10)
	self.frame2 = tk.Frame(self.root, width = 80, height = 10)
	self.frame3 = tk.Frame(self.root, width = 60, height = 50)
	self.frame4 = tk.Frame(self.root, width = 20, height = 50)
	self.canv1 = tk.Canvas(self.frame3)
	self.frame5 = tk.Frame(self.canv1)
	self.but1 = tk.Button(self.frame1, text = 'Новая игра', bg = 'grey')
	self.but2 = tk.Button(self.frame1, text = 'Начать', bg = 'darkgreen')
	self.lab  = tk.Label (self.frame1, font = 'Arial 14', width = 20, height = 5)

#	self.text1 =  tk.Text(self.frame2, width = 55, height = 45, bd = 3)
	self.word = tk.Entry(self.frame2, width = self.frame1.cget('width'), font = 'Arial 20')
	print self.frame1.cget('width')
	self.but3 = tk.Button(self.frame4, text = 'Проверить')



	self.word_scroll = tk.Scrollbar(self.root, command = self.canv1.yview)


	self.mount_widgets()
	self.new_start_game()

	self.word_frame('ворон')

	self.root.mainloop()


    def mount_widgets(self):
	self.frame1.grid(row = 0, column = 0)
	self.frame2.grid(row = 1, column = 0)
	self.frame3.grid(row = 2, column = 0)
	self.word_scroll.grid (row = 2, column = 1)
	self.frame4.grid(row = 2, column = 2)
	self.canv1.pack()
	self.frame5.pack()
	self.but1.grid(row = 0, column = 0, padx = 10)
	self.but2.grid(row = 0, column = 3, padx = 10)
	self.lab.grid(row = 0, column = 1, padx = 10)
#	self.text1.pack()

	self.word.pack()
#	print dir(self.but1)
	self.but3.pack()

#	injected_letters - which letters will enter in new game


    def widgets_newgame(self):
	self.lab.config( text = 'Введите \n слово')
	self.injected_letters = tk.Entry(self.frame1, width = 50, bd = 3, font = 'Arial 14')
	


    def mount_widgets_newgame(self):
#	quit(self.lab)
#	quit(self.ent)
	self.injected_letters.grid(row = 0, column = 2, padx = 10)
	self.injected_letters.focus()

    def widgets_startgame(self):
	self.lab.config( text = 'Введенное \n слово')
#	self.ent = Letters()
	self.injected_letters = tk.Entry(self.frame1, width = 50, bd = 3, font = 'Arial 14')
# !!!	delete this record after create class Letters		!!!




    def mount_widgets_startgame(self):
	self.mount_widgets_newgame()


    def new_start_game(self):
	if self.before_start:
	    self.widgets_newgame()
	    self.mount_widgets_newgame()
	else:
	    self.widgets_startgame()
	    self.mount_widgets_startgame()


    def word_frame(self, word):
	self.word = word
	self.word_del = tk.Button(self.frame3, width = 1, height = 1, text = "x")
	self.word_label = tk.Label(self.frame3, text = self.word , font = 'Arial 12')
	
	self.word_del.pack(side = 'left')
	self.word_label.pack(side = 'right')



    def set_start_game_callback(self, aaaa):
	self.but2.bind("<Button-1>", aaaa)



    def view_getword(self):
	pass




class Letters:
    def __init__(self):
	pass


###		-------------------------
#####			CONTROLLER's part
###		-------------------------

class Controller:
    def __init__(self):
	pass


    def changeWidgets(self):
#	self.view.
	self.model.getWord()

    def todo(self):
	print '/////qweqweqwe//////'












if __name__ == '__main__':
#    root = tk.Tk()
#    app = Controller()
    app = Model()

