def solution():
    # Step 1: Define the words to compare
    word1 = "composition"
    word2 = "composntioi"

    # Step 2: Normalize the words based on the given condition (n = i)
    normalized_word1 = word1.replace("n", "i")
    normalized_word2 = word2.replace("n", "i")

    # Step 3: Compare the normalized words
    if normalized_word1 == normalized_word2:
        result = "0"  # No difference
    else:
        result = "1"  # There is a difference

    # Step 4: Print the result
    print("target :", result)


"""
                ```python
def solution():
    # Step 1: Define the words to compare
    word1 = "composition"
    word2 = "composntioi"
    
    # Step 2: Normalize the words based on the given condition (n = i)
    normalized_word1 = word1.replace("n", "i")
    normalized_word2 = word2.replace("n", "i")
    
    # Step 3: Compare the normalized words
    if normalized_word1 == normalized_word2:
        result = '0'  # No difference
    else:
        result = '1'  # There is a difference
    
    # Step 4: Print the result
    print("target :", result)

solution()
```
"""
