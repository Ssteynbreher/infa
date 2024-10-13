def f(n):   
 if len(n) == 6:
  if n[:3].isalpha() and n[3:].isdigit():
     return "Старый формат"
  else:
     return "Неверный формат"
 if len(n) == 7:
  if n[:1].isdigit() and n[2:4:1].isalpha() and n[5:].isdigit():
     return "Новый формат"
  else:
     return "Неверный формат"

n = input("Введите номерной знак машины: ")
r = f(n)
print(r)
