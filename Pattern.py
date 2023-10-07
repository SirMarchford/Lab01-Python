# Define the size of the pattern
pattern_size = 5  # Adjust the size as needed

# Loop to create and print the pattern
for i in range(pattern_size):
    line = ''
    for j in range(pattern_size):
        if j == i or j == pattern_size - i - 1:
            line += 'X'
            #print("X", end=" ")  # Print an X when the conditions are met
        else:
            line += ' '
            #print(" ", end=" ")  # Print a space for other positions
    print(line * 7)
    #print()  # Move to the next line after each row