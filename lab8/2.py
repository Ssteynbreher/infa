import random
def f():
 n = random.sample(range(1, 50), 6) 
 n.sort()
 return n
b = f()
print(*b)
