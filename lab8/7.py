def f(n):
 sh = snh = s = 0
 n = str(n)
 for i in range(len(n) - 1):
  d = int(n[i])
  if (len(n) - i) % 2 == 0:
   sh += d
  if (len(n) - i) % 2 != 0:
   d *= 2
   if d > 9:
    d -= 9
   snh += d
   s = sh + snh
 return s % 10 == 0
n = input("Введите номер карты: ")
if f(n):
 print("Корректный номер")
else:
 print("Некорректный номер")

