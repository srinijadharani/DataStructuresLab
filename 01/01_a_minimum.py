# 1a. Program to print the minimum of three numbers

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

def smallest_of_all(num1, num2, num3):
    # code to find the smallest of three numbers
    if num1 < num2 and num1 < num3:
        print(num1, "is the smallest number (num1).")
    elif num2 < num1 and num2 < num3:
        print(num2, "is the smallest number (num2).")
    else:
        print(num3, "is the smallest number (num3).")

smallest_of_all(num1, num2, num3)