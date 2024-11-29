def f(x):
    return x[::-1]
file = open("file6.txt", "r",encoding="UTF-8")
content = file.read().split(" ")
content_new = []
for x in content:
    content_new.append(f(x))
print(*content_new)
file.close()