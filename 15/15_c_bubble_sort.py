'''
Write a program to implement various sorting techniques: 
[Compare with Python’s Built-In Sorting Functions also]
• Insertion sort
• Selection Sort
• Bubble Sort
• Merge Sort
• Quick Sort
'''
# BUBBLE SORT
n = int(input("Enter the number of list items: "))
arr = []
for i in range(0, n): 
    ele = int(input("Enter list item: ")) 
    arr.append(ele)

print("Initial array is:", arr)

def bubble(arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
print("Bubble-sorted array is: ", bubble(arr))