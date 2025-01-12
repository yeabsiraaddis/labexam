
def find_matrix_shape(matrix):
    if not matrix or not isinstance(matrix, list):
        return (0, 0)
    
    rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 else 0
    return (rows, columns)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(find_matrix_shape(matrix))  # Output: (3, 3)
