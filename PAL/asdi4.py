def solution():
    # Given inputs
    total_cupcakes_baked = 68
    cupcakes_eaten_by_todd = 32
    cupcakes_per_package = 6

    # Calculate remaining cupcakes after Todd ate some
    remaining_cupcakes = total_cupcakes_baked - cupcakes_eaten_by_todd

    # Calculate how many complete packages can be made
    complete_packages = remaining_cupcakes // cupcakes_per_package

    # Print the result
    print(f"target : {complete_packages}")


"""
                ```python
def solution():
    # Given inputs
    total_cupcakes_baked = 68
    cupcakes_eaten_by_todd = 32
    cupcakes_per_package = 6

    # Calculate remaining cupcakes after Todd ate some
    remaining_cupcakes = total_cupcakes_baked - cupcakes_eaten_by_todd

    # Calculate how many complete packages can be made
    complete_packages = remaining_cupcakes // cupcakes_per_package

    # Print the result
    print(f"target : {complete_packages}")

solution()
```
"""
