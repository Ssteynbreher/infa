n = input()
print("Элементы, которые больше предыдущего:")
if len(n) >= 2:
 p = n[0]
 for i in n[1:]:
  if i > p:

   print(i)
  p = i
else:
 print("В списке меньше двух элементов")
