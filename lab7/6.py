def decode_word(word):
 if word[-1] != '#':
  return "Ошибка! Отсутствует символ #"
 letters = list(word[:-1]) 
 n = len(letters)
 decoded_word = [''] * n 
 for i in range(n):
  decoded_word[i] = letters[((i + 1) % n) - 1] 
 return ''.join(decoded_word) 
encoded_word = input("Введите зашифрованное слово: ")
decoded_word = decode_word(encoded_word)
print(decoded_word)
