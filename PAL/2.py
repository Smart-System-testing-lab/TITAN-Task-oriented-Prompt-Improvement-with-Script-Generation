
def solution():
    # Ask the client how many balls Marin has
    n = int(input("Enter the number of balls Marin has: "))

    # Ask the client how many more balls Ellen has than Marin
    extra_balls = int(input("Enter the number of extra balls Ellen has: "))

    # Calculate the number of balls Ellen has
    ellen_balls = n + extra_balls

    # Provide the client with the calculated number of balls Ellen has
    print(f"Ellen has {ellen_balls} balls.")

# Run the function
solution()

