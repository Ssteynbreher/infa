number = int(input())
first_half_sum = 0
second_half_sum = 0

if len(str(number)) == 6:
 first_half = str(number)[:3]
 second_half = str(number)[3:]

 for digit in first_half:
  first_half_sum += int(digit)
 for digit in second_half:
  second_half_sum += int(digit)

 if first_half_sum == second_half_sum:
  print("Поздравляю! Ваш билет - счастливый")
 else:
  print("Обычный билет")
else:
 print("Некорректный билет")
