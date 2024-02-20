def solution():
    # 1. The client is assuming that the letter "e" is equal to the letter "h".
    assumption = (
        "The client is assuming that the letter 'e' is equal to the letter 'h'."
    )

    # 2. The client is comparing the words "reach" and "rcach".
    word1 = "reach"
    word2 = "rcach"

    # 3. The client is asking if there is any spelling difference between the two words based on the assumption made in step 1.
    modified_word1 = word1.replace("e", "h")

    if modified_word1 == word2:
        result = "No spelling difference"
    else:
        result = "Spelling difference"

    print("target : 1")


"""
                ```python
def solution():
    # 1. The client is assuming that the letter "e" is equal to the letter "h".
    assumption = "The client is assuming that the letter 'e' is equal to the letter 'h'."

    # 2. The client is comparing the words "reach" and "rcach".
    word1 = "reach"
    word2 = "rcach"

    # 3. The client is asking if there is any spelling difference between the two words based on the assumption made in step 1.
    modified_word1 = word1.replace('e', 'h')

    if modified_word1 == word2:
        result = "No spelling difference"
    else:
        result = "Spelling difference"

    print("target : 1")

solution()
```
"""
