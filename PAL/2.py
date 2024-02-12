def solution():
    species_seen = 532
    insect_species = 253
    bird_species = 143

    reptile_species = species_seen - (insect_species + bird_species)

    print("target :", reptile_species)


"""
                Sure, here's a Python function that solves the problem:

```
def solution():
    species_seen = 532
    insect_species = 253
    bird_species = 143

    reptile_species = species_seen - (insect_species + bird_species)

    print("target :", reptile_species)
```

Explanation:

1. We define a function named `solution()` that takes no arguments.
2. We define three variables: `species_seen` (532), `insect_species` (253), and `bird_species` (143).
3. We calculate the number of reptile species by subtracting the sum of insect and bird species from the total number of species seen: `reptile_species = species_seen - (insect_species + bird_species)`.
4. We print the result using the format specified in the question: `print("target :", reptile_species)`.

Note: The function doesn't ask for any input from the user, and it uses the values provided in the question to calculate the number of reptile species.
"""
