# -*- coding: utf-8 -*-


###	colours
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

#print bcolors.WARNING + "Continue?" + bcolors.ENDC
###	/colours

import time
#start = time.time()


###	открытие словаря

import codecs
voc = codecs.open('voc')


dic = []	#	формирование словаря
for i in voc:
    i = i.replace('\n','').decode('utf-8')
    dic.append(i)

voc.close()


###	/открытие словаря


############################################################################################################


###	input

from Tkinter import *

root = Tk()
root.title("-= Anagrams =-")

fra1 = Frame(root, width = 80, height = 10)
fra2 = Frame(root, width = 60, height = 50)
fra3 = Frame(root, width = 20, height = 50)

but1 = Button(fra1,text="Новая игра", bg='grey')
lab1 = Label(fra1, text='Введите \n слово', font="Arial 14", width=20,height=5)
ent = Entry(fra1, width=50, bd=3, font="Arial 14")
but2 = Button(fra1,text="Начать", bg='darkgreen')


tex = Text (fra2, width=55, height = 45, bd=3)


but3 = Button(fra3,text="Проверить")


listOfLetters = ''	# введенное слово


var = IntVar()
var.set(1)

lol = StringVar()
lol.set("")




def quit(self):
    self.destroy()



def new(event):			#	new Game
    var.set(1)
    lol.set = ""
    vvod_gui(var,lab1,ent,listOfLetters)



def vvod(event):		#	ввод слова
    wordFromInput = ent.get()
    print 'wordFromInput =',wordFromInput,'type =',type(wordFromInput)
#    lett = lett.decode('utf-8')
    listOfLetters = list(wordFromInput)
    var.set(2)
    vvod_gui(var,lab1,ent,listOfLetters)
    lol.set(listOfLetters)



def vvod_gui(var,lab,ent,listOfLetters):
    v = var.get()
    print 'v2 =',v
    if v == 1:
	quit(lab)
	quit(ent)
	lab = Label(fra1, text='Введите \n слово', font="Arial 14", width=20,height=5)
	ent = Entry(fra1, width=50, bd=3, font="Arial 14")
	lab.grid(row=0,column=2,padx=10)
	ent.grid(row=0,column=3,padx=10)
	ent.focus()
    else:
	quit(lab)
	quit(ent)
	lab = Label(fra1, text='Введенное \n слово:', font="Arial 14", width=20,height=5)
	ent  = Label(fra1, text=listOfLetters, font = "Arial 20",foreground='red', width=33)
	lab.grid(row=0,column=2,padx=10)
	ent.grid(row=0,column=3,padx=10)
	tex.focus()



def proverka( l, word ):	#	поиск слов в словаре
    w = list(word)
    n = 0
    print 'WWW =',w
    print 'LLL =',l
    for i in w:
	print 'i =',i,'w=',w,'l=',l, 'l_type =', type(l)
	if i in l:
	    l.remove(i)
	    n += 1
    print 'n =',n, 'len(word) = ', len(word)
    if n == len(word):
	print word
	spisok.append(word)
#	print 'letters =', letters

slovar = {}

def dobavka(slovar, slovo):	#	добавить слово в конечный словарь
    w = len(slovo)
    if w in slovar.keys():
        slovar[w].append(slovo)
    else:
        slovar[w] = [slovo]



def sortirovka(spisok):		#	сортировка слов по длине и конечный ВЫВОД
    print 'spisok =',spisok
    spisok.sort()
    for slovo in spisok:
	dobavka(slovar, slovo)
    for i in slovar.keys():
	print bcolors.WARNING + "Слова на ",i," букв: " + bcolors.ENDC, slovar[i]
	print 'Всего слов на ',i,' букв = '

#print bcolors.WARNING + "Continue?" + bcolors.ENDC

start = time.time()

print 'Время поиска:',time.time()-start


def search(event):
    
    for val in dic:
#	let = listOfLetters[:]
	let = lol.get()
	proverka(let, val)
	break
#    sortirovka(spisok)			#	сортировка списка слов/ВКЛЮЧИТЬ!!!


fra1.pack()
fra2.pack(side = LEFT)
fra3.pack(side = LEFT)

#	fra1
#lab.pack(side = LEFT)
#ent.pack(side = LEFT )
#ent.focus()
#but1.pack(side =  LEFT)
but1.grid(row=0,column=1,padx=10)
lab1.grid(row=0,column=2,padx=10)
ent.grid(row=0,column=3)
ent.focus()
but2.grid(row=0,column=4,padx=10)


#	fra2
tex.pack()

#	fra3
but3.pack()

#	binds
but1.bind("<Button-1>",new)
but2.bind("<Button-1>",vvod)
but3.bind("<Button-1>",search)
ent.bind("<Return>", vvod)




root.mainloop()

