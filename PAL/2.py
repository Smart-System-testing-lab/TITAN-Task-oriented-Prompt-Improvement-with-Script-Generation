
def solution():
    # Number of houses
    houses = 8107792
    # Bedrooms per house
    bedrooms_per_house = 3
    # Windows per bedroom
    windows_per_bedroom = 8107792
    # Additional windows per house
    additional_windows = 4

    # Total windows calculation
    total_windows = (houses * bedrooms_per_house * windows_per_bedroom) + (houses * additional_windows)

    # Print the result
    print(f"target: {total_windows:.1f}")

solution()

