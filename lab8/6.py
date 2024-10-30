import random
def sim():
  t = []  
  count = 0  
  while len(t) < 3 or (t[-1] == t[-2] == t[-3]):
    count += 1
    tt = random.choice(["О", "Р"])
    t.append(tt)
    print(tt, end=" ")  
  print("\nРезультат:", ''.join(t))
  return count
a = sim()
print("Количество попыток:", a)

