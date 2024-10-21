def f(n):
 sum = 0
 for i in range(1, n + 1):
  sum += i * i
 return sum
n = int(input("Введите n: "))
res = f(n)
print(res)
