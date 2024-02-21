def solution():
    words = ["csdIM", "cVUDJBfE", "TlToGg"]
    max_unique_letters = 0
    target_word = ""

    for word in words:
        # Normalize data: Convert to lowercase and replace 'd' with 's'
        normalized_word = word.lower().replace("d", "s")
        # Identify unique letters
        unique_letters = set(normalized_word)
        # Count unique letters
        unique_count = len(unique_letters)

        if unique_count > max_unique_letters:
            max_unique_letters = unique_count
            target_word = word

    print(f"target : {target_word}")


"""
                ```python
def solution():
    words = ['csdIM', 'cVUDJBfE', 'TlToGg']
    max_unique_letters = 0
    target_word = ""

    for word in words:
        # Normalize data: Convert to lowercase and replace 'd' with 's'
        normalized_word = word.lower().replace('d', 's')
        # Identify unique letters
        unique_letters = set(normalized_word)
        # Count unique letters
        unique_count = len(unique_letters)

        if unique_count > max_unique_letters:
            max_unique_letters = unique_count
            target_word = word

    print(f"target : {target_word}")

solution()
```
"""
