import random

def f():
  secret = random.randint(1, 10)
  a = 0

  print("Хорошо, я загадал число. Попробуй его отгадать!")

  while True:
    a += 1
    num = int(input("> "))

    if num == secret:
      print("Поздравляю! Вы угадали!")
      break
    else:
      print("Нее, ты не угадал. Попробуй снова!")
      if num < secret:
        print("Загаданное число больше.")
      else:
        print("Загаданное число меньше.")

  print("Количество попыток:", a)

  play = input("Хотите сыграть снова? (да/нет): ")
  if play.lower() == 'да':
    f()

f()

