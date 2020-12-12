'''
Write programs for:
• Representing sparse matrix
• Sparse matrix addition
• Sparse matrix transpose
'''

# Matrix Transpose

matrix = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]] 
print("Initial matrix: ")
for row in matrix: 
    print(row) 
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Transposed matrix: ")
for row in transpose: 
    print(row)