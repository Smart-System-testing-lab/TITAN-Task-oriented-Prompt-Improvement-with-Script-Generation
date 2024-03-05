def solution():
    # Inputs
    area_of_bathroom = 36  # in square feet
    tiles_per_square_foot = 24
    fraction_of_area_covered = 2 / 3

    # Calculation
    area_to_cover = area_of_bathroom * fraction_of_area_covered
    total_tiles_needed = area_to_cover * tiles_per_square_foot

    # Output
    print(f"target: {int(total_tiles_needed)}")


"""
                ```python
def solution():
    # Inputs
    area_of_bathroom = 36  # in square feet
    tiles_per_square_foot = 24
    fraction_of_area_covered = 2 / 3

    # Calculation
    area_to_cover = area_of_bathroom * fraction_of_area_covered
    total_tiles_needed = area_to_cover * tiles_per_square_foot

    # Output
    print(f"target: {int(total_tiles_needed)}")

solution()
```
"""
