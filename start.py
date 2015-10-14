# -*- coding: utf-8 -*-


###	input


lett = raw_input('Введите слово: ' )
lett = lett.decode('utf-8')
lett_tmp = list(lett)



letters = []

for ii in lett_tmp:
    letters.append(ii)



import time
start = time.time()


import codecs
voc = codecs.open('voc')


##	colours

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


###	#1

#dic = {}
#for i in voc:
#    i = i.replace('\n','').decode('utf-8')
#    key = i[0]
#    keys = dic.keys()
#
#    if key in keys:
#	dic[key].append(i)
#    else:
#	dic[key] = [i]
#print keys
#print '='*20
#print dic



###	#2


dic = []
for i in voc:
    i = i.replace('\n','').decode('utf-8')
    dic.append(i)







#start = time.time()-start
#print start


###	search of intersection		###
#start = time.time()


#	выбираем ключи для поиска

#letters_for_key = []
#
#for letter in letters:
#    if letter in letters_for_key:
#	pass
#    else:
#	letters_for_key.append(letter)
#
#
#
#print 'letters_for_key =', letters_for_key



spisok = []


def proverka( l, word ):	#	поиск слов в словаре
    w = list(word)
    n = 0
    for i in w:
	if i in l:
	    l.remove(i)
	    n += 1
    if n == len(word):
#	print word
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
    spisok.sort()
    for slovo in spisok:
	dobavka(slovar, slovo)

    for i in slovar.keys():
	print bcolors.WARNING + "Слова на ",i," букв: "+ bcolors.ENDC, slovar[i]
	print 'Всего слов на ',i,' букв = ',len(slovar[i])

#print bcolors.WARNING + "Continue?" + bcolors.ENDC




for val in dic:
    let = letters[:]
#    print val, type(val)
    proverka(let, val)


sortirovka(spisok)





voc.close()
print 'Время поиска:',time.time()-start
