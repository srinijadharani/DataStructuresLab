# 1c. Program to check whether a given number is perfect or not.

"""Definition: A perfect number is a positive number such that 
it is equal to the sum of its proper divisors."""

num = int(input("Enter a number to check whether it is a perfect number or not: "))

def perfect_number(num):
    # initialize sum to zero in order to increment it later
    sum1 = 0
    # logic to find the sum of the divisors
    for i in range(1, num):
        if num%i == 0:
            sum1 += i
    # check if the number is equal to the sum. if yes, it is a perfect number
    if sum1 == num:
        print(num, "is a perfect number.")
    else:
        print(num, "is not a perfect number.")

perfect_number(num)