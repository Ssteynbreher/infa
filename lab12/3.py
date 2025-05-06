import PySimpleGUI as sg
import random
c_image = [[sg.Image("bio.png")]]
c_input = [[sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
           [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
           [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
           [sg.Button("Рассчитать", font="Arial 20")]]

layout = [
    [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
]

window = sg.Window("Калькулятор бактерий", layout)

while 1:

    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break
    try:
        micro = int(value["micro"])  # начальное количество бактерий
        count = int(value["count"])  # количество секунд
        k = 2  # коэффициент деления
        res = micro  # начальное значение бактерий
        # Основной расчет
        for _ in range(count):
            b = random.randint(0, 4)  # случайное значение b
            res = k * res + b  # обновление количества бактерий
        window["res"].update(res)
    except ValueError:
        sg.popup_error("Введите корректные числа!")
window.close()