def solution():
    quarter_ended_march_31_2015 = {"high_share_price": 101.88, "low_share_price": 93.21}

    percentage_change = (
        (
            quarter_ended_march_31_2015["high_share_price"]
            - quarter_ended_march_31_2015["low_share_price"]
        )
        / quarter_ended_march_31_2015["low_share_price"]
        * 100
    )

    print(f"target: {percentage_change:.4f}")


"""
                Sure, here's a Python function that calculates the percentage change in the share price for the quarter ended March 31, 2015, using the given inputs:
```python
def solution():
    quarter_ended_march_31_2015 = {
        'high_share_price': 101.88,
        'low_share_price': 93.21
    }

    percentage_change = (quarter_ended_march_31_2015['high_share_price'] - quarter_ended_march_31_2015['low_share_price']) / quarter_ended_march_31_2015['low_share_price'] * 100

    print(f'target: {percentage_change:.4f}')
```
The function first defines a dictionary `quarter_ended_march_31_2015` containing the high and low share prices for the quarter ended March 31, 2015. Then, it calculates the percentage change by subtracting the low share price from the high share price, dividing the result by the low share price, and multiplying by 100. Finally, it prints the percentage change to the console using the `print()` function, with the format specifier `%.4f` to display the percentage change to four decimal places.

Note that this function only calculates the percentage change for the quarter ended March 31, 2015, using the given inputs. If you want to calculate the percentage change for other quarters or periods, you'll need to modify the function accordingly or provide additional inputs.
"""
