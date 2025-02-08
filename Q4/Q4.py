# Initialize an empty list to store the heights
heights = []

# Loop until 4 valid heights are entered
while len(heights) < 4:
    # Prompt the user to enter the height of a student
    height = float(input(f"Enter the height of a student {len(heights) + 1} : "))
    
    # Check if the height is within the valid range
    if height < 0:
        print("Height must be positive.")
    elif height > 200:
        print("Height is greater than 200cm.")
    else:
    
        heights.append(height)

# the average height
average_height = sum(heights) / len(heights)

max_height = max(heights)

print("End of input.")
print(f"Average height: {average_height:.2f} cm")
print(f"Maximum height: {max_height:.2f} cm")