# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import os
import wordlist_generator
import merriam_webster

#-----main untility----------------
def submit():
    wordlist=wordlist_generator.get_unknown_words_from(get_input())
    print("start to process"+str(wordlist))
    template=open("./template.html","r")
    output=open("./output.html","w",encoding='utf-8')

    for temp_line in template:

        if temp_line.strip() == "i":
            for x in merriam_webster.get_all_defination(list(wordlist)):
                output.write(x)
        else:
            output.write(temp_line)
    print("work over")
    os.startfile(os.path.normpath("./output.html"))
    template.close()
    output.close()


#-----window init--------------------
root = Tk()
root.title("Modern Vocabulary Manager")
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

input_area=Text(mainframe,width=50,height=30)
input_area.grid(column=0, row=0)


start_button= ttk.Button(mainframe, text='开始处理', command=submit)
start_button.grid(column=0,row=1,sticky=E)
root.resizable(width=False, height=False)

#-----funcional defination-----------

def get_input():
    return set(input_area.get('1.0', 'end').split())

root.mainloop()
