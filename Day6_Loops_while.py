"""
while
while loop we can execute a set of statements as long as a condition is true.
# """
# item = 1  # initialization
# while item < 6: # condition
#   print(item)
#   item += 1    #iteration


# infinite loop
# item = 5  # initialization
# while item < 6: # condition
#   print(item)
#       #iteration

#
# # break keyword
# # With the break statement we can stop the loop even if the while condition is true:
# item = 1
# while item < 10:
#   print(item)
#   if item == 3:
#     break
#   item += 1



# continue :
# With the continue statement we can stop the current iteration, and continue with the next:

# program to print odd numbers from 1 to 10
"""
num = 0

while num < 10:
  num += 1
  if num == 3 and num== 5:
   continue
  print(num)
  
"""
# Input string
input_string = "Guvi Geeks Network Private Limited"

# converting all strings to lowercase to avoide case sesitivity

input_string = input_string.lower()

# Initialize counts for vowels

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

#Iterate through the strings and count vowels

for char in input_string:
    if char == 'a':
        count_a += 1
    elif char == 'e':
        count_e += 1
    elif char == 'i':
        count_i += 1
    elif char == 'o':
        count_o += 1
    elif char == 'u':
        count_u += 1

total_vowels = count_a + count_e + count_i + count_o + count_u

# print the results
print("total number of vowels are :",total_vowels)
print("count of A:", count_a)
print("count of E:", count_e)
print("count of I:", count_i)
print("count of O:", count_o)
print("count of U:", count_u)

# Define the number of rows in the pyramid
num_rows = 5  # You can change this to the number of rows you want in your pyramid

# Calculate the total number of columns needed based on the number of rows
total_cols = num_rows * 2 - 1

# Loop to print the pyramid
for i in range(1, num_rows + 1):
    # Print leading spaces
    for j in range(num_rows - i):
        print(" ", end=" ")

    # Print numbers in ascending order
    for j in range(i, i * 2 - 1):
        print(j, end=" ")

    # Print numbers in descending order (on the right side of the pyramid)
    for j in range(i * 2 - 2, i - 1, -1):
        print(j, end=" ")

    # Move to the next line for the next row
    print()

def remove_vowels(input_string):
    # Initialize an empty string to store the result
    result = ""

    # Define a set of vowels in both uppercase and lowercase
    vowels = "aeiouAEIOU"

    # Iterate through the characters in the input string
    for char in input_string:
        # Check if the character is not a vowel and add it to the result
        if char not in vowels:
            result += char

    return result

# Input string
input_string = input("Enter a string: ")

# Call the function to remove vowels
result_string = remove_vowels(input_string)

# Print the result
print("String with vowels removed:", result_string)
