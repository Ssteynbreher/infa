name_man=open('file8.txt',encoding="UTF-8").readlines()
name_girl=open('file7.txt',encoding="UTF-8").readlines()
count=int(input())
string=input()
if string=='м' or string=='М':
    for i in range(count):
        print(name_man[i])
if string=='ж' or string=='Ж':
    for i in range(count):
        print(name_girl[i])

