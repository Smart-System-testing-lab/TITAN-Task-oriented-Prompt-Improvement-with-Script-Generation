def compare_words_with_substitution(word1, word2, substitution={"b": "n"}):
    # Normalize the input by applying the substitution
    for original, substitute in substitution.items():
        word1 = word1.replace(original, substitute)
        word2 = word2.replace(original, substitute)

    # Sort the characters of both words
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    # Compare the sorted words
    if sorted_word1 == sorted_word2:
        return "0"
    else:
        return "1"


def solution():
    # Assumption: 'b' is equal to 'n'
    substitution = {"b": "n"}

    # First input word
    word1 = "bounce"

    # Second input word
    word2 = "uoucce"

    # Compare the words based on the given assumption
    result = compare_words_with_substitution(word1, word2, substitution)

    print("target :", result)


"""
                ```python
def compare_words_with_substitution(word1, word2, substitution={'b': 'n'}):
    # Normalize the input by applying the substitution
    for original, substitute in substitution.items():
        word1 = word1.replace(original, substitute)
        word2 = word2.replace(original, substitute)
    
    # Sort the characters of both words
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    
    # Compare the sorted words
    if sorted_word1 == sorted_word2:
        return '0'
    else:
        return '1'

def solution():
    # Assumption: 'b' is equal to 'n'
    substitution = {'b': 'n'}
    
    # First input word
    word1 = "bounce"
    
    # Second input word
    word2 = "uoucce"
    
    # Compare the words based on the given assumption
    result = compare_words_with_substitution(word1, word2, substitution)
    
    print("target :", result)

solution()
```
"""
