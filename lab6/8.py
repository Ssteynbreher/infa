binary_number = input("Введите двоичное число: ")
decimal_number = 0
degree = 0

for i in range(len(binary_number) - 1, -1, -1):
 if binary_number[i] == '1':
  decimal_number += 2 ** degree
 degree += 1

print(f"Десятичное представление числа: {decimal_number}")
    