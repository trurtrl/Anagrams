#! /usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import Tkinter as tk


class View:
    def __init__(self,element):
        self.newGame(element)

    def newGame(self, element):
        self.root = tk.Tk()
        self.root.title('-= Anagrams =-')
        self.element = element

        for self.subelement in self.element:
            self.widget_name = self.subelement.tag
#            print 'self.widget_name =', self.widget_name
            self.widget_type = self.set_widget_type()
            self.options = self.set_widget_options(self.subelement)
#            print '|||------  type of options =', type(self.options), 'opt =', self.options
            self.widget_factory = getattr(tk, self.widget_type)
#            print 'self.widget_factory =' ,self.widget_factory, type(self.widget_factory)
            self.mount_point = self.set_mount_point(self.options['parent'])
            del(self.options['parent'])         # only options of widget stay in the dictionary
            self.__dict__[self.widget_name] = self.widget_factory(self.mount_point, **self.options)     # definition properties of a widget
#            print 'widget_attr =', self.subelement.attrib

            print "=========   ", self.__dict__[self.widget_name].__dict__

            for key in self.subelement.attrib.keys():   # assign methods of a widget
#                if key=='grid' or key=='pack':
#                    value = eval(self.subelement.attrib[key])
#                    getattr(self.__dict__[self.widget_name], key)(value)



                value = eval(self.subelement.attrib[key])
                if key=='focus':
                    getattr(self.__dict__[self.widget_name], key)()
                else:
                    getattr(self.__dict__[self.widget_name], key)(value)

#        vcmd = self.register(self.check_ins_symbols), '%d', '%i', '%S'

        self.root.mainloop()
    def set_widget_options(self, subelement):
        self.subelement = subelement
        self.options = {}
        for self.opt_subelement in self.subelement:
            self.options[self.opt_subelement.tag] = self.opt_subelement.text
        return  self.options
    def set_mount_point(self, point):
        self.point = point
        self.mount_point = self.__dict__[self.point]
#        print 'self.mount_point =', self.mount_point,  type(self.mount_point)
        return self.mount_point
    def set_widget_type(self):               #definition type of widget
        self.widget_type = self.subelement.tag.capitalize()
        for i in '1234567890_':
            self.widget_type = self.widget_type.replace(i,'')
#        print 'w_t =', self.widget_type
        return self.widget_type

    def check_ins_symbols(self, symbol):    # Check inserted symbols. They must satisfy my library
        self.my_lib = 'а,б,в,г,д,е,ё,ж,з,и'

        if symbol in self.my_lib:
            print 'symbol =', symbol
        else:
            self.bell()
            print '-- ', symbol, 'is not valid'



class ComposedWord():
    def __init__(self, word):
        self.word = word








#    def widget_factory(selfself,**options):
#        pass

if __name__ == '__main__':
    test = ET.parse('config.xml')
    data = test.getroot()
    window = View(data)
