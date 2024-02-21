def solution():
    # Step 1: Define the words to analyze
    words = ["PMPEPoEG", "UZLfuhw", "YFNOalofXt"]

    # Step 2: Normalize the data
    normalized_words = [word.lower().replace("p", "g") for word in words]

    # Step 3: Identify unique letters and count them
    unique_counts = []
    for word in normalized_words:
        unique_letters = set(
            word
        )  # This automatically ensures 'P' and 'G' are counted as one
        unique_counts.append(len(unique_letters))

    # Step 4 & 5: Determine the word with the greatest number of unique letters
    max_unique_count = max(unique_counts)
    max_index = unique_counts.index(max_unique_count)
    result_word = words[max_index]

    # Step 6: Communicate the findings
    print(f"target : {result_word}")


"""
                ```python
def solution():
    # Step 1: Define the words to analyze
    words = ['PMPEPoEG', 'UZLfuhw', 'YFNOalofXt']
    
    # Step 2: Normalize the data
    normalized_words = [word.lower().replace('p', 'g') for word in words]
    
    # Step 3: Identify unique letters and count them
    unique_counts = []
    for word in normalized_words:
        unique_letters = set(word)  # This automatically ensures 'P' and 'G' are counted as one
        unique_counts.append(len(unique_letters))
    
    # Step 4 & 5: Determine the word with the greatest number of unique letters
    max_unique_count = max(unique_counts)
    max_index = unique_counts.index(max_unique_count)
    result_word = words[max_index]
    
    # Step 6: Communicate the findings
    print(f"target : {result_word}")

solution()
```
"""
