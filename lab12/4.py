import PySimpleGUI as sg
sg.theme('Black')
def to_binary(n, bits=8):
    return bin(n & 0xFF)[2:].zfill(bits)
def to_ones_complement(n, bits=8):
    binary = to_binary(n, bits)
    ones_complement = "".join(['1' if bit == '0' else '0' for bit in binary])
    return ones_complement
def to_twos_complement(n, bits=8):
    binary = to_binary(n, bits)
    ones_complement = to_ones_complement(n, bits)
    twos_complement = bin(int(ones_complement, 2) + 1)[2:].zfill(bits)
    return twos_complement
layout = [
    [sg.Image('img.png', key='-IMAGE-', size=(300, 200))],
    [sg.Text("Введите число (-128...127):")],
    [sg.Input(key="-INPUT-", size=(10, 1))],
    [sg.Button("Рассчитать")],
    [sg.Text("Прямой код:", size=(16, 1)), sg.Output(key="-DIRECT-", size=(10, 1))],
    [sg.Text("Обратный код:", size=(16, 1)), sg.Output(key="-ONES-", size=(10, 1))],
    [sg.Text("Дополнительный код:", size=(16, 1)), sg.Output(key="-TWOS-", size=(10, 1))]
]
window = sg.Window("бебебе", layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Рассчитать":
        try:
            num = int(values["-INPUT-"])
            if -128 <= num <= 127:
                window["-DIRECT-"].update(to_binary(num))
                window["-ONES-"].update(to_ones_complement(num))
                window["-TWOS-"].update(to_twos_complement(num))
            else:
                print("Число должно быть в диапазоне от -128 до 127.")
        except ValueError:
            print("Некорректный ввод. Введите целое число.")
window.close()