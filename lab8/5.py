def fp(h, x):
  p = 0
  for i, r in enumerate(h):
    if x < r:
      p = i
      break
    elif x == r:
      p = i + 1
  return p
h_str = input("Введите росты людей в строю через пробел: ")
h = [int(n) for n in h_str.split()]
x = int(input("Введите рост Андрея: "))

p = fp(h, x)
print("Андрей должен встать на позицию:", p)
