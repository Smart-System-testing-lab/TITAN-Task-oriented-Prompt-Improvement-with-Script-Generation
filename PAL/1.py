def solution():
    # Step 1: Define the assumption
    assumption = {"b": "c", "c": "b"}

    # Step 2: Words for comparison
    word1 = "public"
    word2 = "pullic"

    # Step 3: Apply the assumption to the words
    modified_word1 = "".join(
        [assumption[char] if char in assumption else char for char in word1]
    )
    modified_word2 = "".join(
        [assumption[char] if char in assumption else char for char in word2]
    )

    # Step 4: Compare the modified words
    if modified_word1 == modified_word2:
        result = "0"
    else:
        result = "1"

    # Print the result
    print("target :", result)


"""
                ```python
def solution():
    # Step 1: Define the assumption
    assumption = {'b': 'c', 'c': 'b'}
    
    # Step 2: Words for comparison
    word1 = "public"
    word2 = "pullic"
    
    # Step 3: Apply the assumption to the words
    modified_word1 = ''.join([assumption[char] if char in assumption else char for char in word1])
    modified_word2 = ''.join([assumption[char] if char in assumption else char for char in word2])
    
    # Step 4: Compare the modified words
    if modified_word1 == modified_word2:
        result = '0'
    else:
        result = '1'
    
    # Print the result
    print("target :", result)

solution()
```
"""
