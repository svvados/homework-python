print("Welcome to the Calculator Program!")

# Input user number
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

print("\nPlease select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# User choice
choice = int(input("\nEnter your choice (1-4): "))

# Choose operation
result = 0

if choice == 1:
    result = num1 + num2
elif choice == 2:
    result = num1 - num2
elif choice == 3:
    result = num1 * num2
elif choice == 4:
    result = num1 / num2
else:
    print("Invalid choice!")

# Get result
print("\nThe result is:", result)