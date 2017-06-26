def known_words():
    with open("./word_base.sdb", 'r') as file:
        text = file.read().lower().split()
    return text


def get_unknown_words_from(word_input):
    result=[]
    words_pool = known_words()
    for x in word_input:
        if x.lower() not in words_pool:
            result.append(x)
    return result
            
