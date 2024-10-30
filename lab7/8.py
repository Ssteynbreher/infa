n=input()
teams = n.split('-')
team1 = teams[0].strip()
team2 = teams[1].split()[0].strip()
score = teams[1].split()[1].split(':')
score1 = int(score[0])
score2 = int(score[1])

if score1 > score2:
    print( team1)
elif score2 > score1:
    print (team2)
else:
    print( "Ничья")


