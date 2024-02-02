# Step 1: Define the variables
flour_needed = 12
sugar_needed = 5
flour_put_in = 0

# Step 2: Get the input from the client
flour_put_in = int(input("Enter the number of cups of flour Mary has already put in: "))

# Step 3: Calculate the remaining flour needed
remaining_flour = flour_needed - flour_put_in

# Step 4: Print the result
print("Mary still needs", remaining_flour, "cups of flour.")