# Input: The number n
n = int(input("Enter a positive integer: "))

# Initialize variables
sum_n = 0
i = 1

# Calculate the sum using a while loop
while i <= n:
    sum_n += i
    i += 1

# Output the result
print("The sum of the first", n, "natural numbers is:", sum_n)
