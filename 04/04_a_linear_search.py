# 4a. Program to perform linear search on a list

arr = [6, 3, 7, 2, 8, 9]

print("Given array:")
for i in arr:
    print(i, end = " ")

search_element = int(input("\nEnter the search element: "))

# linear search logic
def linear_search(arr, n):
    count = 0
    while count < len(arr):
        if arr[count] == n:
            return True
        count += 1
    return False

if linear_search(arr, search_element):
    print("Found at index {}." .format(arr.index(search_element)))
else:
    print("Element {} not found." .format(search_element))