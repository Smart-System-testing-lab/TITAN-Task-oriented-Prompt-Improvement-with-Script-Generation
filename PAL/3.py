
import datetime

def solution(date, today):
    # Convert the date to a datetime object
    dt = datetime.datetime.strptime(date, '%m/%d/%Y')

    # Subtract 7 days from the date
    past_date = dt - datetime.timedelta(days=7)

    # Format the past date into MM/DD/YYYY
    past_date_formatted = past_date.strftime('%m/%d/%Y')

    # Return the formatted past date
    return past_date_formatted

# Test the function with the given inputs
print(solution(date='08/03/1997', today=True))


"""
                Sure, here's a Python function that solves the problem:
```python
import datetime

def solution(date, today):
    # Convert the date to a datetime object
    dt = datetime.datetime.strptime(date, '%m/%d/%Y')

    # Subtract 7 days from the date
    past_date = dt - datetime.timedelta(days=7)

    # Format the past date into MM/DD/YYYY
    past_date_formatted = past_date.strftime('%m/%d/%Y')

    # Return the formatted past date
    return past_date_formatted

# Test the function with the given inputs
print(solution(date='08/03/1997', today=True))
```
The function takes two inputs: `date` and `today`. It first converts the `date` string to a `datetime` object using `strptime()`. Then, it subtracts 7 days from the date using `timedelta()`. Finally, it formats the past date into MM/DD/YYYY format using `strftime()` and returns it.

When you run the code, it should print `07/27/1997`, which is the date one week ago from 08/03/1997 in MM/DD/YYYY format.
"""

solution()