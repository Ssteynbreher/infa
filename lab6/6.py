import random

def play_guess_number():
  """Игра "Угадай число"."""
  secret = random.randint(1, 10)
  attempts = 0

  print("Хорошо, я загадал число. Попробуй его отгадать!")

  while True:
    attempts += 1
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

  print("Количество попыток:", attempts)

  play_again = input("Хотите сыграть снова? (да/нет): ")
  if play_again.lower() == 'да':
    play_guess_number()

play_guess_number()

