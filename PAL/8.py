def solution():
    sentence = "Early adopters of LMS technology recognized its potential to transcend traditional classroom boundaries fostering a more flexible and studentcentered learning approach"
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
    sentence = "Early adopters of LMS technology recognized its potential to transcend traditional classroom boundaries fostering a more flexible and studentcentered learning approach"
    words = sentence.split()  # Splitting the sentence into words
    first_letters = [word[0] for word in words]  # Extracting the first letter of each word
    result = ''.join(first_letters)  # Concatenating the first letters to form the final word
    print("target :", result)

solution()
```
"""
