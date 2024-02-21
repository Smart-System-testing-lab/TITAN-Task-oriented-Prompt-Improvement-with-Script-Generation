def solution():
    # Calculate the total time spent driving and hiking
    total_time = 6

    # Determine the average speed at which they drove
    driving_speed = 50

    # Calculate half of the average speed they drove
    half_driving_speed = driving_speed / 2

    # Determine the average speed at which they hiked
    hiking_speed = half_driving_speed - 5

    # Calculate the total time spent hiking
    hiking_time = 1.5

    # Use the formula distance = speed x time to calculate the distance they hiked
    distance_hiked = hiking_speed * hiking_time

    # Calculate the total distance traveled
    total_distance = total_time * driving_speed

    # Calculate the distance to their vacation spot
    distance_to_vacation_spot = total_distance - distance_hiked

    print("target :", distance_to_vacation_spot)


"""
                ```python
def solution():
    # Calculate the total time spent driving and hiking
    total_time = 6

    # Determine the average speed at which they drove
    driving_speed = 50

    # Calculate half of the average speed they drove
    half_driving_speed = driving_speed / 2

    # Determine the average speed at which they hiked
    hiking_speed = half_driving_speed - 5

    # Calculate the total time spent hiking
    hiking_time = 1.5

    # Use the formula distance = speed x time to calculate the distance they hiked
    distance_hiked = hiking_speed * hiking_time

    # Calculate the total distance traveled
    total_distance = total_time * driving_speed

    # Calculate the distance to their vacation spot
    distance_to_vacation_spot = total_distance - distance_hiked

    print("target :", distance_to_vacation_spot)

solution()
```
"""

solution()