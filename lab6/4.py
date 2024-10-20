def f(n):
  for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
  print(" " * (n - 1) + "***")

n = int(input("Введите высоту елочки: "))
f(n)

