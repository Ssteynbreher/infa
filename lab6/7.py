number = int(input())
fs = 0
ss = 0

if len(str(number)) == 6:
 f = str(number)[:3]
 s = str(number)[3:]

 for digit in f:
  fs += int(digit)
 for digit in s:
  ss += int(digit)

 if fs == ss:
  print("Поздравляю! Ваш билет - счастливый")
 else:
  print("Обычный билет")
else:
 print("Некорректный билет")
