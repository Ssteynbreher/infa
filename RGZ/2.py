import PySimpleGUI as sg
import random

# Установка темы интерфейса
sg.theme("DarkPurple1")

# Инициализация счётчиков для игрока и компьютера
p, comp = 0, 0
c_m = 0  # Количество оставшихся раундов
p_name = ''  # Имя игрока

# Определение макета для отображения выбора компьютера
c = [[sg.Image("", key='computer_image')],
     [sg.Text("Ход компьютера", justification='right')]]

# Определение макета для отображения выбора игрока
pep = [[sg.Image("", key='player_image')],
       [sg.Text("Ход игрока", justification='right')]]

# Определение макета для отображения счёта и ввода данных
ost = [[sg.Text('Счёт:')],
       [sg.Text(f"Комьютер {comp}:{p} Игрок ", key="score")],
       [sg.Text('Игрок: '), sg.Input(key="name", size=(29, 1))],
       [sg.Text("Введите количество раундов"), sg.Input(key="c_m", size=(10, 1))],
       [sg.Button('Старт', key='set_matches')],
       [sg.Button('', image_filename='kamen.png', size=(30, 30), key='kamen')],
       [sg.Button('', image_filename='bumaga.png', size=(30, 30), key='bumaga')],
       [sg.Button('', image_filename='noznis.png', size=(30, 30), key='noznis')]]

# Объединение всех макетов в один основной макет окна
layout = [[sg.Column(c, size=(200, 200)), sg.VSeparator(), sg.Column(pep, size=(200, 200)), sg.VSeparator(),
           sg.Column(ost, justification='right')]]

# Создание окна приложения с заданным макетом
window = sg.Window("КМН)", layout)

# Основной цикл обработки событий окна
while True:
    event, values = window.read()

    # Закрытие окна при нажатии на кнопку закрытия
    if event == sg.WIN_CLOSED:
        break

    # Обработка события нажатия кнопки 'Старт'
    if event == 'set_matches':
        try:
            c_m = int(values['c_m'])  # Получение количества раундов от пользователя
            if c_m <= 0:  # Проверка на положительное число
                sg.popup("Введите положительное число!")
                c_m = 0
                continue
            sg.popup(f"Игра будет длиться {c_m} раундов!")  # Уведомление о начале игры
        except ValueError:  # Обработка ошибки преобразования строки в число
            sg.popup("Введите корректное число!")
            continue

    # Обработка выбора игрока (камень, бумага или ножницы)
    if event in ['kamen', 'bumaga', 'noznis']:
        if c_m <= 0:  # Проверка установленного количества раундов
            sg.popup("Установите количество раундов!")
            continue

        player_choice = event  # Сохранение выбора игрока
        computer_choice = random.choice(['kamen', 'bumaga', 'noznis'])  # Случайный выбор компьютера

        # Обновление изображений выбора игрока и компьютера в интерфейсе
        if player_choice == 'kamen':
            window['player_image'].update(filename='kamen.png')
        elif player_choice == 'bumaga':
            window['player_image'].update(filename='bumaga.png')
        else:
            window['player_image'].update(filename='noznis.png')

        if computer_choice == 'kamen':
            window['computer_image'].update(filename='kamen.png')
        elif computer_choice == 'bumaga':
            window['computer_image'].update(filename='bumaga.png')
        else:
            window['computer_image'].update(filename='noznis.png')

        # Определение результата игры и обновление счётчиков
        if player_choice == computer_choice:
            result_text = "Ничья!"
        elif (player_choice == 'kamen' and computer_choice == 'noznis') or (
                player_choice == 'bumaga' and computer_choice == 'kamen') or (
                player_choice == 'noznis' and computer_choice == 'bumaga'):
            result_text = "Вы выиграли!"
            p += 1  # Увеличение счётчика побед игрока
        else:
            result_text = "Вы проиграли!"
            comp += 1  # Увеличение счётчика побед компьютера

        p_name = values['name']  # Сохранение имени игрока
        window['score'].update(f"Компьютер {comp}:{p} Игрок")  # Обновление счёта в интерфейсе

        c_m -= 1  # Уменьшение оставшегося количества раундов

        # Проверка окончания игры и вывод итогового результата
        if c_m == 0:
            sg.popup("Игра завершена!", f"Итоговый счёт: Компьютер {comp} : {p} {p_name}")
            with open("kmngame.txt", "a", encoding="UTF-8") as f:
                f.write(f"Компьютер {comp} : {p} {p_name}\n")  # Запись результатов в файл

            p, comp = 0, 0  # Сброс счётчиков после завершения игры
            window['score'].update(f"Компьютер {comp}:{p} Игрок")  # Обновление счёта в интерфейсе

# Закрытие окна после завершения программы
window.close()
