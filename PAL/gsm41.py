def solution():
    # Inputs
    num_small_coupons = 8236895
    num_big_coupons = 2 * num_small_coupons
    cost_small_coupon = 0.05
    cost_big_coupon = 0.15

    # Calculate total cost
    total_cost = (num_small_coupons * cost_small_coupon) + (
        num_big_coupons * cost_big_coupon
    )

    # Print the result
    print("target :", total_cost)


"""
                ```python
def solution():
    # Inputs
    num_small_coupons = 8236895
    num_big_coupons = 2 * num_small_coupons
    cost_small_coupon = 0.05
    cost_big_coupon = 0.15

    # Calculate total cost
    total_cost = (num_small_coupons * cost_small_coupon) + (num_big_coupons * cost_big_coupon)

    # Print the result
    print("target :", total_cost)

solution()
```
"""
