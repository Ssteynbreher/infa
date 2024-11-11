n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))
matrix = []
print("Введите элементы матрицы:")
for i in range(n):
 row = list(map(int, input().split()))
 if len(row) != m:
  print("Неверный размер строки!")
  exit()
 matrix.append(row)
transposed_matrix = [[matrix[j][i] for j in range(n)] for i in range(m)]
print("Транспонированная матрица:")
for row in transposed_matrix:
 print(*row)
