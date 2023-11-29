import random
import exrex
from random_word import RandomWords
import string
import re

rw = RandomWords()
DATA_COUNT = 400


def repeated():
    words = []
    for _ in range(DATA_COUNT):
        n = random.randint(0, 10)
        if n > 7:
            begin = "".join(random.choices(string.ascii_lowercase, k = random.randint(1, 4)))

            random_key = exrex.getone(rf'({begin}abc{{1,4}}){{3}}')
        else:
            random_key = rw.get_random_word()
        words.append(random_key)
    print(words)


def most_unique_letter(words):
    max_u = 0
    max_u_w = ""

    for word in words:
        k = len(list(set(word.lower())))
        if k > max_u:
            max_u = k
            max_u_w = word
    return max_u_w
    



def most_unique_letter_with_condition( words,a, b):
    batches = []
    max_u = 0
    max_u_w = ""
    for word in words:
        
        new_word = word.lower()
        new_word = str(word).replace(a, b)
        
        k = len(list(set(new_word)))
        if k > max_u:
            max_u = k
            max_u_w = word
    return max_u_w


def find_one_word(pattern, words):
    results = []
    
    for word in words:
        print(word)
        if re.findall(f"(?i){pattern}", word).__len__() == 1:
            results.append(word)
    return results

def find_no_specific_word(words, pattern):
    results = []
    for word in words:
        if re.findall(f'(?i){pattern}', word.lower()).__len__() == 0:
            results.append(word)
    return results

def not_start_with_specific_letter(words, le):
    results = []
    for word in words:
        if word[0].lower() != le:
            results.append(word)
    return results

def not_end_with_specific_letter(words, le):
    results = []
    for word in words:
        if word[-1].lower() != le:
            results.append(word)
    return results