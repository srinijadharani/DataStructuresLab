# 4b. Program to perform binary search on a list

arr = [7, 4, 5, 12, 45, 99, 111, 9876, 987622, 9876]
print("Given array:")
for i in arr:
    print(i, end = " ")

search_element = int(input("\nEnter the search element: "))

# binary search logic
pos = -1
def binary_search(arr, search_element):
    l = 0
    u = len(arr)-1
    
    while l <= u:
        mid = (l + u) // 2
        if arr[mid] == search_element:
            globals()['pos'] = mid
            return True
        
        else:
            if arr[mid] < search_element:
                l = mid+1
            else:
                u = mid-1
    return False
# print the index where the element is found.
if binary_search(arr, search_element):
    print("Found at index {}." .format(pos))
else:
    print("Not found")