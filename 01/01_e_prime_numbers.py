# 1e. Program to print the prime numbers up to a specified limit.

# take the start and end index from the user
start = int(input("Enter the start index: "))  
end = int(input("Enter the stop index: "))  

# function to check if the number is prime or not and then print it
def print_prime(start, end):  
    for num in range(start, end + 1):  
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:  
                print(num, end = " ")

# function call
print_prime(start, end)