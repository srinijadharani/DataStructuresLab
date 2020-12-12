# 2b. Program to copy the contents from one array to another array 
# in reverse order
import array as arr

source_array = arr.array('i', [10, 20, 30, 40])
destination_array = arr.array('i', [])

for index in range(0, len(source_array)):
    destination_array.insert(index, source_array[index])

print("Source array:")
for i in destination_array:
    print(i, end=" ")

print("\nDestination array in reverse order:")
# logic to reverse an array
for i in range(len(source_array)-1, -1, -1):
    destination_array.insert(index, source_array[index])
    print(destination_array[i], end=" ")