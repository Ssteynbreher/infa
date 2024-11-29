def pypypy(fn, wd):
    with open(fn, 'r') as f:
        for ln in f:
            if wd in ln:
                return True
        return False
fls = ["file5.txt", "file6.txt"]
wd = "Academy"
res = ''
for fl in fls:
    if pypypy(fl, wd):
        res = fl
        break
print(f"Слово '{wd}' в файле: {res}")