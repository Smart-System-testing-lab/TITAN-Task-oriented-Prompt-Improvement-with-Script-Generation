
def solution():
    # Given values
    raymond_jewels = 40
    
    # Calculate half of Raymond's jewels
    half_raymond_jewels = raymond_jewels / 2
    
    # Determine Aaron's jewels
    aaron_jewels = half_raymond_jewels + 5
    
    # Find Siobhan's jewels
    siobhan_jewels = aaron_jewels - 2
    
    # Print the result
    print(f"target: {int(siobhan_jewels)}")

solution()

