n = int(input()) 
k = 0 

for i in range(n):
 p, q = map(int, input().split()) 
 if q - p >= 2: 
  k += 1

print(k)

