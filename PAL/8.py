def solution():
<<<<<<< HEAD
    sentence = "All a victim can hope to be is what we already are"
    words = sentence.split()  # Splitting the sentence into words
    first_letters = [
        word[0] for word in words
    ]  # Extracting the first letter of each word
    result = "".join(
        first_letters
    )  # Concatenating the first letters to form the final word
    print("target :", result)
=======
    # Penguins table
    penguins = [
        {"name": "Louis", "age": 7, "height": 50, "weight": 11},
        {"name": "Bernard", "age": 5, "height": 80, "weight": 13},
        {"name": "Vincent", "age": 9, "height": 60, "weight": 11},
        {"name": "Gwen", "age": 8, "height": 70, "weight": 15},
        {"name": "James", "age": 12, "height": 90, "weight": 12},
    ]

    # Giraffes table
    giraffes = [
        {"name": "Jody", "age": 5, "height": 430, "weight": 620},
        {"name": "Gladys", "age": 10, "height": 420, "weight": 590},
        {"name": "Marian", "age": 2, "height": 310, "weight": 410},
        {"name": "Donna", "age": 9, "height": 440, "weight": 650},
    ]

    # Sort giraffes alphabetically
    giraffes_sorted = sorted(giraffes, key=lambda x: x["name"])

    # Get the name
>>>>>>> b536909761d155be40d8dced16aa46d1b86dda0d


"""
                ```python
def solution():
<<<<<<< HEAD
    sentence = "All a victim can hope to be is what we already are"
    words = sentence.split()  # Splitting the sentence into words
    first_letters = [word[0] for word in words]  # Extracting the first letter of each word
    result = ''.join(first_letters)  # Concatenating the first letters to form the final word
    print("target :", result)
=======
    # Penguins table
    penguins = [
        {"name": "Louis", "age": 7, "height": 50, "weight": 11},
        {"name": "Bernard", "age": 5, "height": 80, "weight": 13},
        {"name": "Vincent", "age": 9, "height": 60, "weight": 11},
        {"name": "Gwen", "age": 8, "height": 70, "weight": 15},
        {"name": "James", "age": 12, "height": 90, "weight": 12}
    ]
>>>>>>> b536909761d155be40d8dced16aa46d1b86dda0d

    # Giraffes table
    giraffes = [
        {"name": "Jody", "age": 5, "height": 430, "weight": 620},
        {"name": "Gladys", "age": 10, "height": 420, "weight": 590},
        {"name": "Marian", "age": 2, "height": 310, "weight": 410},
        {"name": "Donna", "age": 9, "height": 440, "weight": 650}
    ]

    # Sort giraffes alphabetically
    giraffes_sorted = sorted(giraffes, key=lambda x: x["name"])

    # Get the name
"""
