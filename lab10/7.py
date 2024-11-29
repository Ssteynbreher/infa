from random import randint
file = open("file6.txt", "r",encoding="UTF-8")
content = file.read().split(" ")
the_first_part,the_second_part=randint(0, len(content)),randint(0, len(content))
print(''.join(content[the_first_part]+content[the_second_part]))
file.close()