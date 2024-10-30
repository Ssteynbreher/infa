n = input()
b = []
c = []
for i in n:
 if i.isalpha():
  b.append(i)
 elif i.isdigit():
  c.append(int(i)) 
print(*b)
print(*c)