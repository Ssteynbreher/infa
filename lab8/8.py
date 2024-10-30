def abb(word):
 if len(word) > 10:
  return word[0] + str(len(word) - 2) + word[-1]
 else:
  return word
n = int(input())
for i in range(n):
 w = input()
 print(abb(w))
