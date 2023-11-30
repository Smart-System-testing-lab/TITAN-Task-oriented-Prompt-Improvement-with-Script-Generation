def change_last_letter_to_z_gpt(word):
    if len(word) > 0:
        modified_word = word[:-1] + 'z'
        return modified_word
    else:
        return "Please provide a word with at least one letter."

def swap_first_second_letters_gpt(word):
    if len(word) > 1:
        swapped_word = word[1] + word[0] + word[2:]
        return swapped_word
    else:
        return "Please provide a word with at least two letters."

def capitalize_first_letter(word):
    if len(word) > 0:
        capitalized_word = word[0].upper() + word[1:]
        return capitalized_word
    else:
        return "Please provide a word with at least one letter."

