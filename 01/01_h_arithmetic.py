# 1g. Program to demonstrate all arithmetic operators in Python

# arithmetic operators: +, -, *, /, //, %, and **
num1 = int(input("Enter the first integer (operand): "))
num2 = int(input("Enter the second integer (operand): "))

def arithmetic_operators(num1, num2):
    print("{} + {} = {}" .format(num1, num2, num1 + num2))
    print("{} - {} = {}" .format(num1, num2, num1 - num2))
    print("{} * {} = {}" .format(num1, num2, num1 * num2))
    print("{} / {} = {}" .format(num1, num2, num1 / num2))
    print("{} // {} = {}" .format(num1, num2, num1 // num2))
    print("{} % {} = {}" .format(num1, num2, num1 % num2))
    print("{} ** {} = {}" .format(num1, num2, num1 ** num2))

arithmetic_operators(num1, num2)