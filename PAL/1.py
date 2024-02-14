def solution():
    # Number of guests at the wedding reception
    n_guests = 100

    # Number of cookies brought by each guest
    n_cookies_per_guest = 2165855

    # Number of cookies given to the church next door
    n_cookies_given_to_church = n_cookies_per_guest // 2

    # Total number of cookies brought to the wedding
    total_cookies = n_guests * n_cookies_per_guest

    # Ratio of cookies to people in the church next door
    cookies_to_people_ratio = n_cookies_given_to_church / total_cookies

    # Number of people in the church next door
    people_in_church = cookies_to_people_ratio * n_guests

    # Print the result
    print(f"target : {people_in_church:.6f}")


"""
                Sure, here's a Python function that solves the problem:
```python
def solution():
    # Number of guests at the wedding reception
    n_guests = 100

    # Number of cookies brought by each guest
    n_cookies_per_guest = 2165855

    # Number of cookies given to the church next door
    n_cookies_given_to_church = n_cookies_per_guest // 2

    # Total number of cookies brought to the wedding
    total_cookies = n_guests * n_cookies_per_guest

    # Ratio of cookies to people in the church next door
    cookies_to_people_ratio = n_cookies_given_to_church / total_cookies

    # Number of people in the church next door
    people_in_church = cookies_to_people_ratio * n_guests

    # Print the result
    print(f"target : {people_in_church:.6f}")
```
Here's how the function works:

1. First, we define the inputs: `n_guests`, `n_cookies_per_guest`, and `n_cookies_given_to_church`.
2. We calculate the total number of cookies brought to the wedding: `total_cookies = n_guests * n_cookies_per_guest`.
3. We calculate the ratio of cookies to people in the church next door: `cookies_to_people_ratio = n_cookies_given_to_church / total_cookies`.
4. We use the ratio to calculate the number of people in the church next door: `people_in_church = cookies_to_people_ratio * n_guests`.
5. Finally, we print the result: `print(f"target : {people_in_church:.6f}")`.

Note that we use the `f` string prefix to format the output as a decimal number with six significant figures.
"""
