def solution():
    regular_hourly_rate = 10
    overtime_multiplier = 1.2
    regular_hours = 40
    total_hours_worked = 45

    # Calculate regular pay
    regular_pay = regular_hourly_rate * regular_hours

    # Calculate overtime pay
    overtime_hours = total_hours_worked - regular_hours
    overtime_hourly_rate = regular_hourly_rate * overtime_multiplier
    overtime_pay = overtime_hourly_rate * overtime_hours

    # Calculate total earnings
    total_earnings = regular_pay + overtime_pay

    print(f"target: {total_earnings}")


"""
                ```python
def solution():
    regular_hourly_rate = 10
    overtime_multiplier = 1.2
    regular_hours = 40
    total_hours_worked = 45
    
    # Calculate regular pay
    regular_pay = regular_hourly_rate * regular_hours
    
    # Calculate overtime pay
    overtime_hours = total_hours_worked - regular_hours
    overtime_hourly_rate = regular_hourly_rate * overtime_multiplier
    overtime_pay = overtime_hourly_rate * overtime_hours
    
    # Calculate total earnings
    total_earnings = regular_pay + overtime_pay
    
    print(f"target: {total_earnings}")

solution()
```
"""
