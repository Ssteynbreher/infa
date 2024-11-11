n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
matrix = [[0 for _ in range(m)] for _ in range(n)]
for j in range(m):
 matrix[0][j] = 1
for i in range(n):
 matrix[i][0] = 1
for i in range(1, n):
 for j in range(1, m):
  matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
for row in matrix:
 for element in row:
  print(f"{element:6d}", end='') 
 print()
