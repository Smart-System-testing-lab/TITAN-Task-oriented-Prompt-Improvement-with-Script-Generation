
def change_last_script(word: str):
    list1 = list(word)

    list1[-1] = "z"

    return "".join(list1)

def swap_first_second_script(word: str):
    list1 = list(word)

    list1[0], list1[1] = list1[1], list1[0]

    return "".join(list1)

def make_first_upper_script(word: str):
    list1 = list(word)

    list1[0] = list1[0].upper()

    return "".join(list1)

def swap_two_words_script(word1: str, word2):

    a = word1[0]
    b = word2[0]
    word2 = a + word2[1:]
    word1 = b + word1[1:]
    return word1, word2

def add_a_script(word):
    return word + "a"

def remove_a_script(word):
    return word.replace("a", "").replace("A","")

def add_letters_together_script(words):
    final = ""
    for word in words:
        final += word[0]

    return final

