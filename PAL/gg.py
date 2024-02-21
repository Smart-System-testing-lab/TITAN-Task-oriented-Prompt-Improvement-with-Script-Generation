def calculate_total_payment(delivery_cost, tip_percentage):
    tip_amount = delivery_cost * tip_percentage
    total_payment = delivery_cost + tip_amount
    return total_payment


def solution():
    delivery_cost = 3821
    tip_percentage = 1 / 5  # Equivalent to 20%
    total_payment = calculate_total_payment(delivery_cost, tip_percentage)
    print(f"target : {total_payment}")


"""
                ```python
def calculate_total_payment(delivery_cost, tip_percentage):
    tip_amount = delivery_cost * tip_percentage
    total_payment = delivery_cost + tip_amount
    return total_payment

def solution():
    delivery_cost = 3821
    tip_percentage = 1/5  # Equivalent to 20%
    total_payment = calculate_total_payment(delivery_cost, tip_percentage)
    print(f"target : {total_payment}")

solution()
```
"""
