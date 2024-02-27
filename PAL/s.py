def extract_and_concatenate(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Extract the first letter of each word and concatenate
    first_letters = "".join(word[0] for word in words)
    return first_letters


def solution():
    # Example sentence
    sentence = "Extract the first letter from each word in the following sentence then concatenate them to form and return the final word Words are separated from each other by spaces"
    # Call the function with the example sentence
    result = extract_and_concatenate(sentence)
    # Print the result
    print("target :", result)


"""
                ```python
def extract_and_concatenate(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Extract the first letter of each word and concatenate
    first_letters = ''.join(word[0] for word in words)
    return first_letters

def solution():
    # Example sentence
    sentence = "Extract the first letter from each word in the following sentence then concatenate them to form and return the final word Words are separated from each other by spaces"
    # Call the function with the example sentence
    result = extract_and_concatenate(sentence)
    # Print the result
    print("target :", result)

solution()
```
"""
