n = int(input("Введите размер матрицы: "))
matrix = []
print("Введите элементы матрицы:")
for i in range(n):
 row = list(map(int, input().split()))
 if len(row) != n:
  print("Неверный размер строки!")
  exit()
 matrix.append(row)
for i in range(n):
 matrix[i][i], matrix[i][n - i - 1] = matrix[i][n - i - 1], matrix[i][i]
# Вывод измененной матрицы
print("Измененная матрица:")
for row in matrix:
 print(*row)
