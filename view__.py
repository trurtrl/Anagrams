#! /usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk



class BaseWindow:
    def __init__(self, before_start = True):
	self.before_start = before_start
	self.root = tk.Tk()
	self.root.title('-= Anagrams =-')

	self.field1()
	self.field1_mount()
	self.field2()
	self.field2_mount()
	self.field3()
	self.field3_mount()
	self.scroll()
	self.scroll_mount()
	self.field4()
	self.field4_mount()



	self.root.mainloop()


    def field1(self):
	self.frame1 = tk.Frame(self.root, width = 80, height = 10)
	self.but11 = tk.Button(self.frame1)
	self.lab11 = tk.Label (self.frame1, font = 'Arial 14', width = 20, height = 5)


	print self.frame1.cget('width')

	self.frame1.grid(row = 0, column = 0)
	self.field1_dynamic()

    def field1_dynamic(self):
	if self.before_start:
	    self.but11.config(text = 'Начать', bg = 'darkgreen')
	    self.lab11.config( text = 'Введите \n слово')
	    self.injected_letters = tk.Entry(self.frame1, width = 60, bd = 3, font = 'Arial 14')
	    self.injected_letters.focus()
	else:
	    self.but11.config(text = 'Заново')
	    self.lab11.config( text = 'Введенное \n слово')
	    self.injected_letters = tk.Label(self.frame1, width = 60, bd = 3, font = 'Arial 20', fg = 'red')
#	    self.injected_letters.config( text = self.    )

    def field1_mount(self):
	self.lab11.grid(row = 0, column = 0, padx = 10)
	self.injected_letters.grid(row = 0, column = 1, padx = 10)
	self.but11.grid(row = 0, column = 2, padx = 10)










    def field2(self):
	self.frame2 = tk.Frame(self.root, width = 80, height = 10)
	self.word = tk.Entry(self.frame2, width = self.frame1.cget('width'), font = 'Arial 20')
    def field2_mount(self):
	self.frame2.grid(row = 1, column = 0)
	self.word.pack()

    def field3(self):
	self.frame3 = tk.Frame(self.root, width = 60, height = 50)
	self.canv3 = tk.Canvas(self.frame3, width = 60, height = 50)
	self.frame31= tk.Frame(self.canv3 ,width = 60, height = 50)
    def field3_mount(self):
	self.frame3.grid(row = 2, column = 0)
	self.canv3.pack()
	self.frame31.pack()

    def scroll(self):
	self.word_scroll = tk.Scrollbar(self.root, command = self.canv3.yview)
    def scroll_mount(self):
	self.word_scroll.grid (row = 2, column = 1)

    def field4(self):
	self.frame4 = tk.Frame(self.root, width = 20, height = 50)
	self.but41  = tk.Button(self.frame4, text = 'Проверить')
    def field4_mount(self):
	self.frame4.grid(row = 2, column = 2)
	self.but41.pack()






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


if __name__ == '__main__':
    bw = BaseWindow()

