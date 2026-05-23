# Function to find the lowest and second lowest numbers
def find_lowest(numbers):

    # Sort the list from smallest to biggest
    numbers.sort()

    # The first number is the lowest
    lowest = numbers[0]

    # The second number is the second lowest
    low = numbers[1]

    # Return both numbers as a tuple
    return (lowest, low)


# Example list
nums = [8, 3, 1, 6, 2]

# Calling the function
answer = find_lowest(nums)

# Display the result
print(answer)