import re

#game = "A2B2A1B2A2B1A2B2A1B2A1A1B1A1A2"
game = input()

players = re.split('1|2', game)
points = re.split('A|B', game)

#print(players)
#print(points)

alice = 0
barb = 0

for i in range(len(players)):
    if (players[i] == 'A'):
        alice += int(points[i+1])
    elif (players[i] == 'B'):
        barb += int(points[i+1])

#print(alice)
#print(barb)

if (alice > barb):
    print('A')
else:
    print('B')

    
