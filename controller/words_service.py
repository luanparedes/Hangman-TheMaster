from random import randint as rd


class Word:
    doc = '../words.txt'

    def get_word(self):
        with open(self.doc, 'rt') as f:
            list_of_words = f.readlines()
            word = list_of_words[rd(0, len(list_of_words) -1)]

            return word
