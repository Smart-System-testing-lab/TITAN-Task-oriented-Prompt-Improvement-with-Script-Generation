def solution():
    treetown_donation = 570.00
    forest_reserve_donation = 140.00
    animal_preservation_park_donation = forest_reserve_donation - 140.00
    total_donation = (
        treetown_donation + forest_reserve_donation + animal_preservation_park_donation
    )
    print(f"Total amount donated to all three parks: ${total_donation}")


"""
                Sure, here's a Python function that solves the problem:
```python
def solution():
    treetown_donation = 570.00
    forest_reserve_donation = 140.00
    animal_preservation_park_donation = forest_reserve_donation - 140.00
    total_donation = treetown_donation + forest_reserve_donation + animal_preservation_park_donation
    print(f"Total amount donated to all three parks: ${total_donation}")
```
Explanation:

1. First, we define the three variables for the donations to Treetown National Park, the Forest Reserve, and Animal Preservation Park, respectively.
2. We calculate the total donation by adding the three variables.
3. Finally, we print the total donation using the `print()` function.

Note: The `f` string notation is used to include the calculated total donation in the string.
"""
