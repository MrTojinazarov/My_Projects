def FindMaxSquare(matrix):
    if not matrix:
        return 0
    
    n = len(matrix)
    m = len(matrix[0])
    
    new_matrix = [[0] * m for _ in range(n)]
     
    max_side = 0
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    new_matrix[i][j] = 1
                else:
                    new_matrix[i][j] = min(new_matrix[i-1][j], new_matrix[i][j-1], new_matrix[i-1][j-1]) + 1
 
                max_side = max(max_side, new_matrix[i][j])
    
    print(new_matrix)
    
    return max_side * max_side

matrix = [
    [1, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0]
]

# Sample 1

# matrix = [
#     [0, 1],
#     [1, 0],
# ]

# Sample 2
# matrix = [
#     [1, 1, 0, 1, 0],
#     [1, 1, 1, 1, 1],
#     [0, 1, 1, 1, 0],
# ]


result = FindMaxSquare(matrix)

print(f"Natija: {result}")
