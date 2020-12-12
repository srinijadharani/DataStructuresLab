# 1b. Program to find the GCD and LCM of two/three numbers.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

def hcf_lcm(num1, num2):
    # code to find the hcf of two numbers
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller+1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
    print("HCF of {} and {} is {}." .format(num1, num2, hcf))

    # logic to find the lcm from computed hcf
    lcm = (num1*num2)/hcf
    print("LCM of {} and {} is {}." .format(num1, num2, int(lcm)))


hcf_lcm(num1, num2)