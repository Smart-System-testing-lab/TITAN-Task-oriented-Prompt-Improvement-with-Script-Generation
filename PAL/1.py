def solution():
    total_puppies = 9 + 12  # Calculate total number of puppies available for adoption
    adoption_rate = 3  # Number of puppies adopted per day
    days_to_adopt = (
        total_puppies // adoption_rate
    )  # Calculate number of days to adopt all puppies
    print(f"Target: {days_to_adopt}")  # Print the result


"""
                Sure, here's a Python function that solves the problem:

```python
def solution():
    total_puppies = 9 + 12  # Calculate total number of puppies available for adoption
    adoption_rate = 3  # Number of puppies adopted per day
    days_to_adopt = total_puppies // adoption_rate  # Calculate number of days to adopt all puppies
    print(f"Target: {days_to_adopt}")  # Print the result
```

Explanation:

1. First, we calculate the total number of puppies available for adoption by adding the number of puppies initially in the shelter (9) to the number of additional puppies brought in (12). This gives us a total of 21 puppies.
2. Next, we calculate the number of days it would take to adopt all the puppies by dividing the total number of puppies available for adoption by the number of puppies adopted per day. In this case, we have 21 / 3 = 7.
3. Finally, we print the result in the format requested by the client: "Target: X", where X is the number of days it would take to adopt all the puppies.

Note: The // operator is used for integer division, which is what we want in this case since we're dealing with whole numbers. If you prefer to use decimal division, you can replace // with /.
"""
