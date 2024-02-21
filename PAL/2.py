
def solution():
    # Fixed and variable costs for Venue 1
    fixed_cost_venue_1 = 200
    variable_cost_per_guest_venue_1 = 5
    
    # Cost per guest for Venue 2
    cost_per_guest_venue_2 = 25
    
    # Equation: 200 + 5 * Number of Guests = 25 * Number of Guests
    # Solve for Number of Guests
    number_of_guests = (fixed_cost_venue_1) / (cost_per_guest_venue_2 - variable_cost_per_guest_venue_1)
    
    # Print the result
    print(f"target: {int(number_of_guests)}")

solution()

