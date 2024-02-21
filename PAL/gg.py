def solution():
    # Given data
    daily_trips = 5085340
    days_per_week = 5
    cost_per_trip = 2.20
    weekly_pass_cost = 20

    # Calculate the total cost of bus trips without the pass
    total_cost_without_pass = daily_trips * days_per_week * cost_per_trip

    # Calculate the savings by buying a weekly bus pass
    savings = total_cost_without_pass - weekly_pass_cost

    # Print the result
    print(f"target : {savings}")


"""
                ```python
def solution():
    # Given data
    daily_trips = 5085340
    days_per_week = 5
    cost_per_trip = 2.20
    weekly_pass_cost = 20
    
    # Calculate the total cost of bus trips without the pass
    total_cost_without_pass = daily_trips * days_per_week * cost_per_trip
    
    # Calculate the savings by buying a weekly bus pass
    savings = total_cost_without_pass - weekly_pass_cost
    
    # Print the result
    print(f"target : {savings}")

solution()
```
"""
