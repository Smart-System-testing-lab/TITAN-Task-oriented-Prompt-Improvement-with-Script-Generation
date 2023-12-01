def counting_with_condition(words):
    return len(words)


def counting_words(sentences):
    return len(sentences.split())

def counting_words_condition_script(sentences):
    count = 0
    s = sentences.split()
    for i in s:
        if len(i) > 2:
            count += 1
    return count
def count_lower_case_script(word):
    count = 0
    for i in word:
        if str(i).isupper():
            continue
        count += 1
    return count

def count_lower_case_specific_script(word, s):
    count = 0
    for i in word:
        if i.isupper() or s != i:
            continue
        count += 1
    return count

def count_specific_letter_script(words, letter):
    return words.lower().count(letter)



def count_vowel_script(word):
    word = str(word.lower())
    return word.count("a") + word.count("i") + word.count("o") + word.count("u") + word.count("e")

def count_digits_in_number_script(number):

    result = len([1 for char in number if char.isdigit()])
    return result

