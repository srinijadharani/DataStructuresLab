# 2c. Program to delete duplicate elements from an array

# import the array module
import array as arr
array1 = arr.array("i", [1, 3, 6, 6, 8, 1, 9, 4, 3, 0, 4])
# initial array
print("Initial array is:")
for a in array1:
    print(a, end = ", ")
# function to delete duplicate elements
def delete_duplicate(array1):
    array2 = arr.array("i", [])
    for num in array1: 
        if num not in array2: 
            array2.append(num) 
    print("\nArray after deleting the duplicate elements is:")
    for i in array2:
        print(i, end = ", ")

delete_duplicate(array1)