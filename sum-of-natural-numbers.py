# Write a Python Program to Find the Sum of Natural Numbers.

num = int(input("Enter the limit: "))
# Initialize the sum
sum = 0
# Use a for loop to calculate the sum of natural numbers
for i in range(1, num + 1):
 sum += i
# Print the sum
print("The sum of natural numbers up to", num, "is:", sum)