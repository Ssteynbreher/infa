import random
def generate_magic(n):
  magic = [[0 for _ in range(n)] for _ in range(n)]
  number = 1
  row = 0
  col = n // 2
  while number <= n**2:
    magic[row][col] = number
    number += 1
    next_row = (row - 1) % n
    next_col = (col + 1) % n
    if magic[next_row][next_col] != 0:
      row = (row + 1) % n
    else:
      row = next_row
      col = next_col

  return magic

n = int(input("Введите порядок магического квадрата: "))
magic = generate_magic(n)

for row in magic:
  print(*row)
