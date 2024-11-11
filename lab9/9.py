import random
def cf():
  f = [['.' for _ in range(4)] for _ in range(4)]
  s = 4
  while s > 0:
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    if f[r][c] == '.':
      f[r][c] = ','
      s -= 1
  while True:
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    if f[r][c] == '.':
      f[r][c] = ','
      break
  return f
def pf(f):
  for r in f:
    print(' '.join(r))
def gs():
  while True:
    try:
      r, c = map(int, input("Введите координаты выстрела (строка, столбец): ").split())
      if 0 <= r <= 3 and 0 <= c <= 3:
        return r, c
      else:
        print("Неверные координаты. Попробуйте снова.")
    except ValueError:
      print("Неверный формат ввода. Попробуйте снова.")
def pg():
  f = cf()
  sh = 0
  sl = 4
  while sl > 0:
    pf(f)
    r, c = gs()
    sh += 1
    if f[r][c] == ',':
      f[r][c] = 'X'
      sl -= 1
      print("Попадание!")
    elif f[r][c] == '':
      print("Вы взорвались! Игра окончена.")
      return False, sh
    else:
      print("Мимо!")
  print("Поздравляем! Вы потопили все корабли за", sh, "ходов.")
  return True, sh
if __name__ == "__main__":
  w, sh = pg()
  if w:
    print("Вы победили!")
  else:
    print("Вы проиграли!")

