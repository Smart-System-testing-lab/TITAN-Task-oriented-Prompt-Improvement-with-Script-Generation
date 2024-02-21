def solution():
    # Step 1: Define the words and the assumption
    word1 = "lighthouse"
    word2 = "nighthouse"
    assumption = {"l": "n", "n": "l"}

    # Step 2: Apply the assumption to both words
    transformed_word1 = "".join([assumption.get(char, char) for char in word1])
    transformed_word2 = "".join([assumption.get(char, char) for char in word2])

    # Step 3: Compare the transformed words
    if transformed_word1 == transformed_word2:
        result = "target : 0"
    else:
        result = "target : 1"

    print(result)


"""
                ```python
def solution():
    # Step 1: Define the words and the assumption
    word1 = "lighthouse"
    word2 = "nighthouse"
    assumption = {"l": "n", "n": "l"}
    
    # Step 2: Apply the assumption to both words
    transformed_word1 = "".join([assumption.get(char, char) for char in word1])
    transformed_word2 = "".join([assumption.get(char, char) for char in word2])
    
    # Step 3: Compare the transformed words
    if transformed_word1 == transformed_word2:
        result = "target : 0"
    else:
        result = "target : 1"
    
    print(result)

solution()
```
"""
