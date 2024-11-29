file=open("file4.txt",encoding="UTF-8").readlines()
array=set()
for x in file:
    text=x.strip().split(" ")
    array.add(int(text[2]))
array=sorted(array)[::-1]
for x in file:
    text=x.strip().split(" ")
    if array[1]==int(text[2]):
        print(*text)
        exit()
