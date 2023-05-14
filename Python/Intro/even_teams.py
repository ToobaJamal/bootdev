'''
red_team should have the players with even-numbered indexes
blue_team should have the players with odd-numbered indexes
'''

players = ["Harry", "Hermione", "Ron", "Ginny", "Fred", "Neville", "Draco", "Luna", "Cho", "Gregory", "Lee", "Michael", "Lavender", "Parvati", "Padma", "Colin", "Dennis", "George", "Allan", "John", "Hunter", "Angelina", "Lee", "Katie", "Susan", "Alicia", "Frank", "Anthony"]

# Don't touch above this line

red_team = players[::2]
blue_team = players[1::2]

# Don't touch below this line

print(f"Red team has {len(red_team)} players")
print(f"Blue team has {len(blue_team)} players")
