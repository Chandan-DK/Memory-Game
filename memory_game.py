import os
from random_words import RandomWords


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def generate_word_list(num_words):
    rw = RandomWords()
    words_set = set()
    while len(words_set) != num_words:
        word = rw.random_word()
        words_set.add(word)
    word_list = list(words_set)
    return word_list


clear_screen()
input("Hit Enter To Start The Game...")
clear_screen()


# Generate words for memorization
num_words = int(input("Enter the number of words to memorize: "))
original_word_list = generate_word_list(num_words+10)
words_to_memorize = original_word_list[:num_words]