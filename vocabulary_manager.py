#  -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import os
import re

#functional import
import wordlist_generator
import merriam_webster

def unique(items):
    found = set([])
    keep = []

    for item in items:
        if item not in found:
            found.add(item)
            keep.append(item)

    return keep

# -----window init--------------------
root = Tk()
root.title("Modern Vocabulary Manager | version 1.2 (17.2.26)")
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)

control_panel=ttk.Frame(mainframe)
control_panel.grid(column=3,row=0,sticky=N)

input_area = Text(mainframe, width=50, height=30)
input_area.grid(column=0, row=0)



#--------commont words----------------
##onevar=BooleanVar()
##onevar.set(True)
##one=ttk.Checkbutton(mainframe,text="check button",variable=onevar,onvalue=True)
##one.grid(column=1,row=0)

#--------Radiobutton----------

extert_button = ttk.Button(control_panel, text='提取单词')
extert_button.grid(column=0, row=0)

select_button = ttk.Button(control_panel, text='开始生成')
select_button.grid(column=0, row=1)

##
##dict_MW=ttk.Radiobutton(control_panel, text='Merrian Webster')
##dict_MW.grid(column=0,row=2)

#---------list box------------
name_list=StringVar(value=["先在左侧输入单词"])
wordlist=Listbox(mainframe,height=10,
                     listvariable=name_list,
                     selectmode=MULTIPLE,
                     activestyle='none',
                     selectbackground ="#fff",
                     selectforeground="#999")
wordlist.grid(column=1, row=0, sticky=(N,S,E,W))

#------scoll bar for list box-------------

bar_for_list=ttk.Scrollbar(mainframe,orient=VERTICAL,command=wordlist.yview)
wordlist['yscrollcommand']=bar_for_list.set
bar_for_list.grid(column=2,row=0,sticky=(N,S))


#从 listbox 中获得所有的项目
#print(wordlist.get(0,last=wordlist.size()))
#-----main untility-------------------
global_list=[]
def auto_get_known_words():
    global global_list
    global wordlist
    global_list=unique(wordlist_generator.get_unknown_words_from(get_input()))
    name_list.set(global_list)
    
def user_selected_known_words():
    return [global_list[x] for x in range(len(global_list)) if x not in  wordlist.curselection()] 


def submit():
    delete_empty=lambda strings:[x for x in strings if x]
    word_list=delete_empty(user_selected_known_words())
    
    print("Start to process:\n  " + str(word_list)+"\n")
    template = open("./template.html", "r")
    output = open("./output.html", "w", encoding='utf-8')

    for temp_line in template:
        if temp_line.strip() == "i":
            for x in merriam_webster.get_all_defination(word_list):
                output.write(x)
        else:
            output.write(temp_line)
    print("\nDictionary generateed successfully")
    os.startfile(os.path.normpath("./output.html"))
    template.close()
    output.close()

extert_button.configure(command=auto_get_known_words)
select_button.configure(command=submit)


#------functional definition-------------

def get_input():
    return list(re.split(" |,|\n|\.|\?|!",input_area.get('1.0', 'end').replace(u"\u2018", " ").replace(u"\u2019", " ")))

root.resizable(width=False, height=False) 
root.mainloop()