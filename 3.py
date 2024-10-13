n = int(input())
d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
print(n + d1 + d2)