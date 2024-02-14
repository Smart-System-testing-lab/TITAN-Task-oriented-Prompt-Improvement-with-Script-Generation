def solution():
    Emilys_shrimp_peeling_rate = 6
    Emilys_shrimp_sauting_rate = 30 / 10
    number_of_shrimp = 90

    time_to_peel = number_of_shrimp / Emilys_shrimp_peeling_rate
    time_to_saut = number_of_shrimp / Emilys_shrimp_sauting_rate

    total_time = time_to_peel + time_to_saut

    print(f"Target: {total_time}")


"""
                Sure, here's a Python function that solves the problem:
```python
def solution():
    Emilys_shrimp_peeling_rate = 6
    Emilys_shrimp_sauting_rate = 30 / 10
    number_of_shrimp = 90

    time_to_peel = number_of_shrimp / Emilys_shrimp_peeling_rate
    time_to_saut = number_of_shrimp / Emilys_shrimp_sauting_rate

    total_time = time_to_peel + time_to_saut

    print(f"Target: {total_time}")
```
Explanation:

1. We define the inputs as variables: Emilys shrimp peeling rate, Emilys shrimp sautéing rate, and the number of shrimp to be peeled and cooked.
2. We calculate the time it takes Emily to peel the shrimp by dividing the number of shrimp by her peeling rate.
3. We calculate the time it takes Emily to sauté the shrimp by dividing the number of shrimp by her sautéing rate.
4. We add the time it takes to peel and sauté the shrimp to get the total time.
5. We print the total time it will take Emily to peel and cook 90 shrimp.

The output of the function will be:
```
Target: 45
```
This means that it will take Emily 45 minutes to peel and cook 90 shrimp.
"""
