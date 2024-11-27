def get_keypad_sequence(text):
    keypad = {
        'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333',
        'g': '4', 'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555',
        'm': '6', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777',
        's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99',
        'y': '999', 'z': '9999',
        '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
        '7': '7', '8': '8', '9': '9', '0': '0',
        ' ': '00'
    }
    sequence = ""
    for char in text.lower():
        if char in keypad:
            sequence += keypad[char] + ""
    return sequence.strip()
if __name__ == "__main__":
    message = input("Введите текст: ")
    keypad_seq = get_keypad_sequence(message)

    if keypad_seq:
        print(keypad_seq)
    else:
        print("Ошибка!")
