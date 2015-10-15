#! /usr/bin/python
# -*- coding: utf-8 -*-


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_startGameCB(self.startGame)
        self.view.set_newGameCB(self.newGame)

        self.view.root.mainloop()

    def changeWidgets(self):
#	self.view.
	self.model.getWord()


    def startGame(self):
        self.model.set_xxx(self.view.getLetters())
        self.view.before_start = False
        self.view.field1_dynamic()





    def newGame(self):
        pass

    def todo(self):
	print '/////qweqweqwe//////'





