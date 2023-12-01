def count_a_in_word_gpt(word):
    if len(word) > 0:
        count = word.lower().count('a')
        return count
    else:
        return "Please provide a word with at least one letter."

def count_vowels_in_word_gpt(word):
    if len(word) > 0:
        vowels = "aeiouAEIOU"
        count = sum(1 for letter in word if letter in vowels)
        return count
    else:
        return "Please provide a word with at least one letter."


def count_lowercase_letters_gpt(word):
    if len(word) > 0:
        lowercase_count = sum(1 for letter in word if letter.islower())
        return lowercase_count
    else:
        return "Please provide a word with at least one letter."
    

def count_characters_in_word_gpt(word):
    if len(word) > 0:
        total_characters = len(word)
        return total_characters
    else:
        return "Please provide a word with at least one character."

def count_specific_letter_in_word_gpt(word, letter):
    if len(word) > 0:
        letter_count = word.lower().count(letter.lower())
        return letter_count
    else:
        return "Please provide a word with at least one letter."


def count_digits_in_number_gpt(number):
        # Convert the number to a string and count digits
    number_str = number
    digit_count = sum(1 for char in number_str if char.isdigit())
    return digit_count

