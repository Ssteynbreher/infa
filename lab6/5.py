def dog_age_to_human(dog_age):
  if dog_age < 0:
    return "Ошибка!"
  elif dog_age <= 2:
    return dog_age * 10.5
  else:
    return 21 + (dog_age - 2) * 4

# Получение собачьего возраста от пользователя
dog_age = int(input("Введите собачий возраст: "))

# Вычисление и вывод человеческого возраста
human_age = dog_age_to_human(dog_age)
print("Введенный вами год эквивалентен", human_age, "человеческим")

