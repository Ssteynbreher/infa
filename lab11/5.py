import PySimpleGUI as sg
sg.theme('DarkBrown7')
def calculate_score(word):
    letter_scores = {
        'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10,
        'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
        'd': 2, 'g': 2,
        'b': 3, 'c': 3, 'm': 3, 'p': 3,
        'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
        'k': 5,
        'j': 8, 'x': 8,
        'q': 10, 'z': 10,
    }
    total_score = 0
    for letter in word.lower():
        if letter in letter_scores:
            total_score += letter_scores[letter]
        else:
            return 0
    return total_score
layout = [
    [sg.Image('pngwing.com.png', key='-IMAGE-', size=(450, 250))],
    [sg.Text("Введите слово:")],
    [sg.Input(key="-WORD-")],
    [sg.Button("Рассчитать"), sg.Button("Выход")],
    [sg.Text("", key="-OUTPUT-", size=(50, 1))]
]
window = sg.Window("Калькулятор очков для Эрудита", layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Выход":
        break
    if event == "Рассчитать":
        word = values["-WORD-"]
        score = calculate_score(word)
        window["-OUTPUT-"].update(f"Количество очков: {score}")
window.close()
