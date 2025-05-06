count=int(input())
array=[]
for i in range(0,count):
    array.append(input().split(" "))
    array[i][1]=array[i][1].replace('woman','1').replace('captain','3').replace('man','2')\
        .replace('child','1')
for a,b in array:
    if b=='1':
        print(a)
for a, b in array:
    if b == '2':
        print(a)
for a, b in array:
    if b == '3':
        print(a)
