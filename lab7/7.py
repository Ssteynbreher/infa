import random
def generate_password(length, uppercase, lowercase, digits, symbols):
  characters = ""
  if uppercase:
    characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  if lowercase:
    characters += "abcdefghijklmnopqrstuvwxyz"
  if digits:
    characters += "0123456789"
  if symbols:
    characters += "!@#$%^&*()_+-={}[]|\:;'<>,.?/~`"

  if not characters:
    return "Ошибка: Не выбраны символы для пароля"

  password = ''.join(random.choice(characters) for i in range(length))
  return password
length = int(input("Введите желаемую длину пароля: "))
uppercase = input("Нужны ли заглавные буквы (да/нет)? ").lower() == 'да'
lowercase = input("Нужны ли строчные буквы (да/нет)? ").lower() == 'да'
digits = input("Нужны ли цифры (да/нет)? ").lower() == 'да'
symbols = input("Нужны ли специальные символы (да/нет)? ").lower() == 'да'
password = generate_password(length, uppercase, lowercase, digits, symbols)
print("Сгенерированный пароль:", password)
