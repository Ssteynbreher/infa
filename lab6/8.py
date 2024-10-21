binn = input("Введите двоичное число: ")
dec = 0
res = 0

for i in range(len(binn) - 1, -1, -1):
 if binn[i] == '1':
  dec += 2 ** res
 res += 1

print(f"Десятичное представление числа: ", dec)
    
