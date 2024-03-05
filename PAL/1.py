def solution():
    # Given inputs
    words = ["IcYuiiurr", "ajoqd", "mxWuiiuPZ"]
    sequence = "uiiu"

    # Iterate through each word to check for the sequence
    for word in words:
        if sequence not in word:
            result = f"target : {word}"
            break

    print(result)


"""
                ```python
def solution():
    # Given inputs
    words = ['IcYuiiurr', 'ajoqd', 'mxWuiiuPZ']
    sequence = "uiiu"
    
    # Iterate through each word to check for the sequence
    for word in words:
        if sequence not in word:
            result = f"target : {word}"
            break
    
    print(result)

solution()
```
"""
