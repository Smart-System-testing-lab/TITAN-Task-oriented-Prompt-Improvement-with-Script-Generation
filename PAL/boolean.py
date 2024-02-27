def solution():
    initial_cost_per_minute = 1.0
    reduced_cost_per_minute = 0.2
    duration_for_initial_cost = 16
    total_call_duration = 36

    if total_call_duration <= duration_for_initial_cost:
        cost = total_call_duration * initial_cost_per_minute
    else:
        initial_cost = duration_for_initial_cost * initial_cost_per_minute
        remaining_duration = total_call_duration - duration_for_initial_cost
        reduced_cost = remaining_duration * reduced_cost_per_minute
        cost = initial_cost + reduced_cost

    print(f"target : {cost}")


"""
                ```python
def solution():
    initial_cost_per_minute = 1.0
    reduced_cost_per_minute = 0.2
    duration_for_initial_cost = 16
    total_call_duration = 36

    if total_call_duration <= duration_for_initial_cost:
        cost = total_call_duration * initial_cost_per_minute
    else:
        initial_cost = duration_for_initial_cost * initial_cost_per_minute
        remaining_duration = total_call_duration - duration_for_initial_cost
        reduced_cost = remaining_duration * reduced_cost_per_minute
        cost = initial_cost + reduced_cost

    print(f"target : {cost}")

solution()
```
"""
