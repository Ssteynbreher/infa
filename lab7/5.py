def g(n):
    k=0
    glas='уеэоаыяиюЮИЯЭОАЫЕУ'
    for i in range(len(n)):
        if n[i] in glas:
            k+=1
    return k
n = input()
s = n.split('/')
if len(s)==3:
    if s[0]==5  and s[1]==7 and s[2]==5:
        print('Хайку!')
    else:
        print('Не хайку!')
else:
    print('Не хайку. Должно быть 3 строки.')