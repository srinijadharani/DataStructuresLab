# 1g. Program to swap two numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The numbers before swapping are - num1: {} and num2: {}." .format(num1, num2))

# logic for swapping two numbers 
num1, num2 = num2, num1

print("The numbers after swapping are - num1: {} and num2: {}." .format(num1, num2))