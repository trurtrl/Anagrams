#! /usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk

class BaseWindow:
    def __init__(self, before_start = True):
        self.before_start = before_start
        self.root = tk.Tk()
        self.root.title('-= Anagrams =-')

        self.field1()
        self.field2()
        self.field3()
        self.scroll()
        self.scroll_mount()
        self.field4()
        self.field4_mount()

        self.startGameCallback = None
        self.newGameCallback = None


#        self.root.mainloop()


    def field1(self):
        self.frame1 = tk.Frame(self.root, width = 80, height = 10)
        self.but11 = tk.Button(self.frame1)
        self.lab11 = tk.Label (self.frame1, font = 'Arial 14', width = 20, height = 5)

        print self.frame1.cget('width')

        self.frame1.grid(row = 0, column = 0)
        self.field1_dynamic()

    def field1_dynamic(self):
        if self.before_start:
            self.but11.config(text = 'Начать', bg = 'darkgreen', command = self.startGame )
            self.lab11.config( text = 'Введите \n слово')
            self.injected_letters = tk.Entry(self.frame1, width = 70, bd = 3, font = 'Arial 14')
            self.injected_letters.focus()
        else:
#           self.but11.destroy()
            self.but11.config(text = 'Заново', command = self.newGame )
            self.lab11.config(text = 'Введенное \n слово')
            self.injected_letters = tk.Label(self.frame1, width = 70, bd = 3, font = 'Arial 20', fg = 'red')
            self.injected_letters.config( text = self.letters)
        self.field1_mount()

    def field1_mount(self):
        self.lab11.grid(row = 0, column = 0, padx = 10)
        self.injected_letters.grid(row = 0, column = 1, padx = 10)
        self.but11.grid(row = 0, column = 2, padx = 10)



    def field2(self):
        self.frame2 = tk.Frame(self.root, width = 80, height = 10)
        self.word = tk.Entry(self.frame2, width = self.frame1.cget('width'), font = 'Arial 20')
        self.field2_mount()
    def field2_mount(self):
        self.frame2.grid(row = 1, column = 0)
        self.word.pack()

    def field3(self):
        self.frame3 = tk.Frame(self.root, width = 60, height = 50)
        self.canv3 = tk.Canvas(self.frame3, width = 60, height = 50)
        self.frame31= tk.Frame(self.canv3 ,width = 60, height = 50)
        self.field3_mount()
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

    def set_startGameCB(self, call):
        self.startGameCallback = call

    def set_newGameCB(self, call):
        self.newGameCallback = call

    def startGame(self):
        if self.startGameCallback:
            self.startGameCallback()
#        self.zz = self.injected_letters.get()
#        print self.zz

    def newGame(self):
        if self.newGameCallback:
            self.newGameCallback()



    def getLetters(self):
        self.letters = self.injected_letters.get()
#        print 'letters =', self.letters
        return self.letters





if __name__ == '__main__':
    bw = BaseWindow()






