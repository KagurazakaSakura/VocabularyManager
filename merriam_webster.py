# -*- coding: utf-8 -*-
import urllib.request
import re
print("webster dictionary start")
def request_xml(word):
    r = urllib.request.urlopen("http://www.dictionaryapi.com/api/v1/references/learners/xml/" + word + "?key=508b6e11-3920-41fe-a57a-d379deacf188").read().decode("utf-8")
    print("gets success:"+word)
    if len(r)<=83:
        return None
    else:
        content = r[69:][:-15].splitlines()
        return [i.strip() for i in content]

def have_resource_of(content):
    if content is None:
        return False
    else:
        return True

def vaild_check(lines):
    if lines[0][0:5]=="<sugg":
        return False
    else:
        return True

def isWord(entry,word):
    aux_i=0
    duration=[]
    for i,x in enumerate(entry):
        if x=="\"":
            duration.append(i)
            aux_i+=1
            if aux_i==2:
                break
    entry_name=entry[(duration[0] + 1):(duration[1])]
    fully_match=(entry_name == word)
    part_match=(re.search(word + "(\[\d\])+",entry_name) is not None)

    return fully_match or part_match

def get_all_defination(word_list):
    for word in word_list:
        word_xml=request_xml(word)
        if have_resource_of(word_xml):
            if vaild_check(word_xml):
                for entry in word_xml:
                    if isWord(entry,word):
                        yield entry
                        break
            else:
                print("形式错误"+word)



