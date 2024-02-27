def solution():
    # The client mentioned the letters "n" and "w" being equal.
    # The client asked about the spelling difference between "downtown" and "doodtood" assuming the equality of "n" and "w".

    word1 = "downtown"
    word2 = "doodtood"

    # Replace 'n' with 'w' in both words
    word1 = word1.replace("n", "w")
    word2 = word2.replace("n", "w")

    # Check if the words are the same
    if word1 == word2:
        result = "0"
    else:
        result = "1"

    print("target :", result)


"""
                ```python
def solution():
    # The client mentioned the letters "n" and "w" being equal.
    # The client asked about the spelling difference between "downtown" and "doodtood" assuming the equality of "n" and "w".
    
    word1 = "downtown"
    word2 = "doodtood"
    
    # Replace 'n' with 'w' in both words
    word1 = word1.replace('n', 'w')
    word2 = word2.replace('n', 'w')
    
    # Check if the words are the same
    if word1 == word2:
        result = '0'
    else:
        result = '1'
    
    print("target :", result)

solution()
```
"""
