max1=0
min1=100000
for n in range(1,10000):
    n=int(input())
    if n==0:
       break
    else:
       max1=max(n,max1)
       min1=min(n,min1)
print("Самый высокий человек с ростом: ", max1, "Самый низкий человек с ростом: ", min1)