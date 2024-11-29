file = open("file1.txt", "r",encoding="UTF-8")
content = file.read().split(" ")
count=int(len(content)/2)
new_text=input()
content[count]=content[count]+' '+new_text
print(content[count])
print(" ".join(content))
file.close()
