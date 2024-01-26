import os
import random
import time
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


def display_words(words):
    num_columns = 2
    column_width = max(len(word) for word in words) + 4
    for i, word in enumerate(words, 1):
        print(f"{word:{column_width}}", end="")
        if i % num_columns == 0:
            print()
    time.sleep(len(words) + 10)
    clear_screen()


def get_user_input(word):
    while True:
        user_input = input(f"Is '{word}' in the original word list? (y/n): ").lower()
        if user_input == "y" or user_input == "n":
            return user_input


def get_score(user_input, word, words_to_memorize):
    return (
        1
        if (
            (user_input == "y" and word in words_to_memorize)
            or (user_input == "n" and word not in words_to_memorize)
        )
        else 0
    )


def test_user(original_word_list, words_to_memorize):
    total_score = 0
    random.shuffle(original_word_list)
    answer_list = []
    for word in original_word_list:
        print(f"Is '{word}' in the original word list?")
        user_input = get_user_input(word)
        score = get_score(user_input, word, words_to_memorize)
        total_score += score
        answer_list.append((word, user_input, "✅" if score == 1 else "❌"))
        clear_screen()
    return total_score, answer_list


def display_words_to_memorize(words):
    print("Actual Words:\n")
    num_columns = 2
    column_width = max(len(word) for word in words) + 4
    for i, word in enumerate(words, 1):
        print(f"{word:{column_width}}", end="")
        if i % num_columns == 0:
            print()


def display_answers_list(data):
    print("\nYour Answers:\n")
    column_width = max(len(word) for word, _, _ in data) + 2
    for word, answer, mark in data:
        print(f"{word:{column_width}} {answer} {mark}")

    
def display_total_score(total_score, num_words):
    print(f"Total Score: {total_score}/{num_words}")


clear_screen()
input("Hit Enter To Start The Game...")
clear_screen()


# Generate words for memorization
num_words = int(input("Enter the number of words to memorize: "))
original_word_list = generate_word_list(num_words+10)
words_to_memorize = original_word_list[:num_words]


# Memorization phase
print("Memorize the following words:\n")
display_words(words_to_memorize)
input("Press Enter to start the test...")


# Testing phase
total_score, answer_list = test_user(original_word_list, words_to_memorize)


# Display memorized words, user answers, and total score
display_words_to_memorize(words_to_memorize)
display_answers_list(answer_list)
display_total_score(total_score, num_words)