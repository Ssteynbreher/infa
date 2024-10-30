n = []
while 1:
  s = input("Введите число: ")
  if s == "":
    break
  n.append(int(s))

if len(n) > 0:
  a = sum(n) / len(n)
  print("Среднее значение:", a)

  print("Числа ниже среднего:")
  for i in n:
    if i < a:
      print(i)

  print("Числа выше среднего:")
  for i in n:
    if i > a:
      print(i)
else:
  print("Ошибка")

