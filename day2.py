# Read the input file line by line, ignoring empty lines
with open('input.txt', 'r') as file:
    data = [line.strip() for line in file if line.strip()]

# Initialize a counter for unsafe reports
unSafe = 0

# Function to check if a report is safe
def is_safe(report):
    # Variable to track whether the sequence is increasing or decreasing (initially unknown)
    is_increasing = None  
    
    # Loop through the list to analyze pairs of numbers
    for j in range(len(report) - 1):
        num1 = report[j]
        num2 = report[j + 1]
        
        # Calculate the absolute difference between consecutive numbers
        difference = abs(num1 - num2)
        
        # Check if the difference is out of the allowed range (>3 or equal to 0)
        if difference > 3 or difference == 0:
            return False
        
        # Determine the sequence direction (increasing or decreasing) during the first iteration
        if is_increasing is None:
            is_increasing = num1 < num2
        
        # Verify that the sequence direction remains consistent
        if (num1 < num2) != is_increasing:
            return False
    
    return True

# Iterate through each line of data
for line in data:
    # Split the line into integers and store them in a list
    newList = list(map(int, line.split()))
    
    # Check if the report is already safe
    if is_safe(newList):
        continue
    
    # Check if removing one level makes the report safe
    safe_with_removal = False
    for idx in range(len(newList)):
        # Create a new list excluding the current index
        modified_list = newList[:idx] + newList[idx + 1:]
        if is_safe(modified_list):
            safe_with_removal = True
            break
    
    # If not safe even after removing one level, mark as unsafe
    if not safe_with_removal:
        unSafe += 1

# Calculate the number of safe reports as the total minus the unsafe ones
safe = len(data) - unSafe

# Print the number of safe reports
print(safe)
