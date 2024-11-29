import string
def pypypy(file):
    try:
        with open(file, 'r') as f:
            text = f.read()
            words = text.split()
            total_words = len(words)
            e_words = 0
            for word in words:
              word = word.strip(string.punctuation)
              if 'e' in word.lower():
                  e_words += 1
            if total_words > 0:
                e_pr = (e_words / total_words) * 100
            else:
                e_pr = 0.0
            return e_pr
    except FileNotFoundError:
        print(f"Ошибка: файл '{file}' не найден.")
        return None
if __name__ == "__main__":
    file = "file6.txt"
    pr = pypypy(file)
    if pr is not None:
        print(f"{pr:.2f}%")