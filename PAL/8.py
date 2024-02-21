def solution():
    sentence = "All a victim can hope to be is what we already are"
    words = sentence.split()  # Splitting the sentence into words
    first_letters = [
        word[0] for word in words
    ]  # Extracting the first letter of each word
    result = "".join(
        first_letters
    )  # Concatenating the first letters to form the final word
    print("target :", result)


"""
                ```python
def solution():
    sentence = "All a victim can hope to be is what we already are"
    words = sentence.split()  # Splitting the sentence into words
    first_letters = [word[0] for word in words]  # Extracting the first letter of each word
    result = ''.join(first_letters)  # Concatenating the first letters to form the final word
    print("target :", result)

solution()
```
"""
