def f(x):
 return x**2
def t(a, b, N):
 h = (b - a) / N # Шаг интегрирования
 sum = 0
 for i in range(1, N):
  x = a + i * h
  sum += f(x)
 return (h / 2) * (f(a) + f(b) + 2 * sum)
a = float(input("Введите нижний предел интегрирования: "))
b = float(input("Введите верхний предел интегрирования: "))
for N in [10, 100, 1000]:
 res = t(a, b, N)
 print(f"Интеграл для N = {N}: {res}")

