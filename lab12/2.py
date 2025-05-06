word = input().strip()
if word[0]=='Q' and (word.count('Q')==word.count('A')) and word[-1] != 'Q':
    print('+')
else:
    print('-')