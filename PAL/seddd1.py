def solution():
    # Inputs mentioned in the client's query
    words = ["soprawsartdo", "fwtsarnzqnjl"]

    # Request to swap the opening characters of the two words
    new_words = [words[1][0] + words[0][1:], words[0][0] + words[1][1:]]

    # Print the output
    print(f"target : {new_words}")


"""
                ```python
def solution():
    # Inputs mentioned in the client's query
    words = ['soprawsartdo', 'fwtsarnzqnjl']
    
    # Request to swap the opening characters of the two words
    new_words = [words[1][0] + words[0][1:], words[0][0] + words[1][1:]]
    
    # Print the output
    print(f"target : {new_words}")

solution()
```
"""
