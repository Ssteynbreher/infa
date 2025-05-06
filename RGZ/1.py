import PySimpleGUI as sg
import random

sg.theme("DarkPurple1")
p, comp = 0, 0
c_m = 0
p_name = ''
c = [[sg.Image("", key='computer_image')],
     [sg.Text("Ход компьютера", justification='right')]]
pep = [[sg.Image("", key='player_image')],
       [sg.Text("Ход игрока", justification='right')]]
ost = [[sg.Text('Счёт:')], [sg.Text(f"Комьютер {comp}:{p} Игрок ", key="score")],
       [sg.Text('Игрок: '), sg.Input(key="name", size=(29, 1))],
       [sg.Text("Введите количество раундов"), sg.Input(key="c_m", size=(10, 1))],
       [sg.Button('Старт', key='set_matches')],
       [sg.Button('', image_filename='kamen.png', size=(30, 30), key='kamen')],
       [sg.Button('', image_filename='bumaga.png', size=(30, 30), key='bumaga')],
       [sg.Button('', image_filename='noznis.png', size=(30, 30), key='noznis')]]

layout = [[sg.Column(c, size=(200, 200)), sg.VSeparator(), sg.Column(pep, size=(200, 200)), sg.VSeparator(),
           sg.Column(ost, justification='right')]]
window = sg.Window("КМН)", layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'set_matches':
        try:
            c_m = int(values['c_m'])
            if c_m <= 0:
                sg.popup("Введите положительное число!")
                c_m = 0
                continue
            sg.popup(f"Игра будет длиться {c_m} раундов!")
        except ValueError:
            sg.popup("Введите корректное число!")
            continue
    if event in ['kamen', 'bumaga', 'noznis']:
        if c_m <= 0:
            sg.popup("Установите количество раундов!")
            continue
        player_choice = event
        computer_choice = random.choice(['kamen', 'bumaga', 'noznis'])
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

        if player_choice == computer_choice:
            result_text = "Ничья!"
        elif (player_choice == 'kamen' and computer_choice == 'noznis') or (
                player_choice == 'bumaga' and computer_choice == 'kamen') or (
                player_choice == 'noznis' and computer_choice == 'bumaga'):
            result_text = "Вы выиграли!"
            p += 1
        else:
            result_text = "Вы проиграли!"
            comp += 1
        p_name = values['name']
        window['score'].update(f"Компьютер {comp}:{p} Игрок")
        c_m -= 1
        if c_m == 0:
            sg.popup("Игра завершена!", f"Итоговый счёт: Компьютер {comp} : {p} {p_name}")
            with open("kmngame.txt", "a", encoding="UTF-8") as f:
                f.write(f"Компьютер {comp} : {p} {p_name}\n")
            p, comp = 0, 0
            window['score'].update(f"Компьютер {comp}:{p} Игрок")
window.close()