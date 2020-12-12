# 1f. Program to find the sum of digits of a number. 
# Check whether given number is Armstrong number or not.

num = int(input("Enter a number: "))
# function to find the sum of digits in the give number
def sum_of_digits(num):
    temp1 = num
    sum1 = 0
    while temp1 != 0:
        sum1 += temp1 % 10
        temp1 //= 10
    print("Sum of the given number {} is {}." .format(num, sum1))

# armstrong number of a 3 digit number is such that the sum of cubes of its digits is equal to the number itself.

def armstrong(num):
    temp2 = num
    sum2 = 0
    while temp2 != 0:
        last_digit = temp2 % 10
        sum2 += pow(last_digit, 3)
        temp2 //= 10
    if sum2 == num:
        print("The given number {} is an Armstrong Number." .format(num))
    else:
        print("The given number {} is not an Armstrong Number." .format(num))
    
# function calls
sum_of_digits(num)
armstrong(num)