def known_words():
    with open("./word_base.sdb",'r') as file:
        text=set(file.read().split())
    return text

def get_unknown_words_from(word_input):
    return word_input - known_words()
