# Read the input file line by line, ignoring empty lines
data = [line for line in open('input.txt', 'r').read().split('\n') if line.strip()]

# Initialize a counter for unsafe reports
unSafe = 0

# Iterate through each line of data
for i in data:
    # Split the line into integers and store them in a list
    newList = list(map(int, i.split()))
    
    # Variable to track whether the sequence is increasing or decreasing (initially unknown)
    is_increasing = None  
    
    # Loop through the list to analyze pairs of numbers
    for j in range(len(newList) - 1):
        num1 = newList[j]
        num2 = newList[j + 1]
        
        # Calculate the absolute difference between consecutive numbers
        difference = abs(num1 - num2)
        
        # Check if the difference is out of the allowed range (>3 or equal to 0)
        if difference > 3 or difference == 0:
            unSafe += 1  # Mark the report as unsafe
            break  # Exit the loop for this report
        
        # Determine the sequence direction (increasing or decreasing) during the first iteration
        if is_increasing is None:
            is_increasing = num1 < num2
        
        # Verify that the sequence direction remains consistent
        if (num1 < num2) != is_increasing:
            unSafe += 1  # Mark the report as unsafe
            break  # Exit the loop for this report

# Calculate the number of safe reports as the total minus the unsafe ones
safe = len(data) - unSafe

# Print the number of safe reports
print(safe)
