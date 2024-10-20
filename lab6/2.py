def a(start, end):
 total = 0
 for i in range(start, end + 1):
  if i % 2 == 0: 
   total += i
 return total
otv = a(2, 100)

print("Сфинкс, ответ на твою загадку:", otv)
