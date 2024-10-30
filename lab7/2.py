n=input("Введите два слова: ") 
if n.count(' ')==1:
    w1, w2 = n.split()
    print(w2, w1)
else:
    print("Ошибка!")
