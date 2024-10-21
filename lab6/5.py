def f(n):
  if n < 0:
    return "Ошибка!"
  elif n <= 2:
    return n * 10.5
  else:
    return 21 + (n - 2) * 4
n = int(input("Введите возраст: "))
h = f(n)
print("Введенный вами год эквивалентен", h, "человеческим")

