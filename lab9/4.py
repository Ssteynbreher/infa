menu = [
  ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
  ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
  ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
]
def show_menu():
 print("Меню:")
 for i, dish in enumerate(menu):
  print(f"{i+1}. {dish[0]} - {dish[1]}, цена: {dish[2]}")
def find_dish(dish_name):
 for dish in menu:
  if dish[0] == dish_name:
   print(f"Ингредиенты: {dish[1]}, цена: {dish[2]}")
   return
 print(f"Блюдо '{dish_name}' не найдено в меню.")
def add_dish():
 dish_name = input("Введите название блюда: ")
 ingredients = input("Введите ингредиенты (через запятую): ").split(",")
 price = int(input("Введите цену: "))
 menu.append([dish_name, ingredients, price])
 print(f"Блюдо '{dish_name}' добавлено в меню.")
def change_price():
 dish_name = input("Введите название блюда: ")
 for dish in menu:
  if dish[0] == dish_name:
   new_price = int(input("Введите новую цену: "))
   dish[2] = new_price
   print(f"Цена блюда '{dish_name}' изменена на {new_price}.")
   return
 print(f"Блюдо '{dish_name}' не найдено в меню.")
while True:
 print("1. Отобразить меню")
 print("2. Найти блюдо")
 print("3. Добавить новое блюдо")
 print("4. Изменить цену блюда")
 print("5. Выход")
 choice = input("Введите номер действия: ")
 if choice == "1":
  show_menu()
 elif choice == "2":
  dish_name = input("Введите название блюда: ")
  find_dish(dish_name)
 elif choice == "3":
  add_dish()
 elif choice == "4":
  change_price()
 elif choice == "5":
  break
 else:
  print("Неверный выбор.")