def known_words():
    with open("./word_base.sdb", 'r') as file:
        text = set(file.read().split())
    return text


def get_unknown_words_from(word_input):
    words_pool = known_words()
    for x in word_input:
        if x in words_pool:
            yield x
