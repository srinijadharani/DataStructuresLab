# 2a. Program to read a linear list of items and store it in an array.
# Copy the contents from one array to another array.

# import the array module
import array as arr

source_array = arr.array("i", [10, 20, 30, 40, 50])
destination_array = arr.array("i", []) # create an empty array

print("Source array:")
for s in source_array:
    print(s, end = " ")

# logic to copy elements of one array on to another
for i in range(0, len(source_array)):
    destination_array.insert(i, source_array[i])

print("\nDestination array after copying the elements from source array:")
for n in destination_array:
    print(n, end = " ")
