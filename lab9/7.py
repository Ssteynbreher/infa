n = int(input("Введите количество рядов: "))
m = int(input("Введите количество мест в ряду: "))
k = int(input("Введите количество билетов в заказе: "))
seats = []
print("Введите информацию о занятости мест (0 - свободно, 1 - занято):")
for i in range(n):
 row = list(map(int, input().split()))
 if len(row) != m:
  print("Неверный размер строки!")
  exit()
 seats.append(row)
found_row = 0
for i in range(n):
 for j in range(m - k + 1):
  if all(seats[i][j + l] == 0 for l in range(k)):
   found_row = i + 1
   break 
 if found_row:
  break 
print(found_row)
