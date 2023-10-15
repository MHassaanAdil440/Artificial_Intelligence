matrix1 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]

matrix2 = [[1, 2, 1],
           [4, 5, 6],
           [9, 8, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for row in result:
    print(row)
