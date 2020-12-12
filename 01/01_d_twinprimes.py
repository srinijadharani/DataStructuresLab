# 1d. Program to print twin primes upto a specified limit

start = int(input("Enter the starting index from which you want to print twin primes: "))
end = int(input("Enter the end index: "))
# check whether the number in the range of start and end
def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
# print the twin primes
def twin_primes(start, end):
    for i in range(start, end):
        j = i + 2
        if(prime(i) and prime(j)):
            print("({}, {})" .format(i, j))

twin_primes(start, end)