import string
import random

def load_words():
    WORDLIST_FILENAME = "words.txt"
    print "Loading word list from file..........."
    inFile = open(WORDLIST_FILENAME, 'r',)
    line = inFile.readline()
    word_list = string.split(line)
    print "  ", len(word_list), "words loaded.\n"

    return word_list
def choose_word():
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word