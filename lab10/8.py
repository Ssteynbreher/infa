n=int(input())
m=int(input())
k=0
for i in range(n):
    if i%2==0:
        print("#"*m)
        continue
    if k==0:
        print('.'*(m-1)+'#')
        k+=1
    else:
        print('#'+'.' * (m - 1))
        k=0