def solution():
    pam_roller_coaster_rides = 9401149
    fred_roller_coaster_rides = 4
    pam_luge_rides = 9401149
    fred_luge_rides = 9401149
    cost_per_ride = 6

    total_pam_tickets = (
        pam_roller_coaster_rides * cost_per_ride + pam_luge_rides * cost_per_ride
    )
    total_fred_tickets = (
        fred_roller_coaster_rides * cost_per_ride + fred_luge_rides * cost_per_ride
    )

    total_tickets = total_pam_tickets + total_fred_tickets

    print(f"Target: {total_tickets}")


"""
                Sure, here's a Python function that solves the problem:

```python
def solution():
    pam_roller_coaster_rides = 9401149
    fred_roller_coaster_rides = 4
    pam_luge_rides = 9401149
    fred_luge_rides = 9401149
    cost_per_ride = 6

    total_pam_tickets = pam_roller_coaster_rides * cost_per_ride + pam_luge_rides * cost_per_ride
    total_fred_tickets = fred_roller_coaster_rides * cost_per_ride + fred_luge_rides * cost_per_ride

    total_tickets = total_pam_tickets + total_fred_tickets

    print(f"Target: {total_tickets}")
```

The function takes no input, as all the necessary values are provided in the question. It calculates the total number of tickets used by Pam and Fred for both roller coaster and luge rides, and then adds them up to give the total number of tickets used that day. Finally, it prints the result in the format requested.
"""
