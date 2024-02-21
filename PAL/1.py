def solution():
    # Step 1: Define the words
    word1 = "suggest"
    word2 = "suggesg"

    # Step 2: Replace 't' with 'e' in both words to normalize them based on the given condition
    normalized_word1 = word1.replace("t", "e")
    normalized_word2 = word2.replace("t", "e")

    # Step 3: Compare the normalized words
    if normalized_word1 == normalized_word2:
        result = "0"
    else:
        result = "1"

    # Step 4: Print the result
    print("target :", result)


"""
                ```python
def solution():
    # Step 1: Define the words
    word1 = "suggest"
    word2 = "suggesg"
    
    # Step 2: Replace 't' with 'e' in both words to normalize them based on the given condition
    normalized_word1 = word1.replace('t', 'e')
    normalized_word2 = word2.replace('t', 'e')
    
    # Step 3: Compare the normalized words
    if normalized_word1 == normalized_word2:
        result = '0'
    else:
        result = '1'
    
    # Step 4: Print the result
    print("target :", result)

solution()
```
"""
