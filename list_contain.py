'''
Our players have requested an in-game feature that will allow them to type in a weapon name to check if it's in the list of top weapons in the realm.

Take a look at the 3 print statements. 
Replace the static boolean values in the curly braces with an in statement that checks if the weapon in the text is in the top_weapons list.

Look at the text of each print statement to decide which weapon to check for.
'''

top_weapons = [
    "sword of justice",
    "sword of slashing",
    "stabby daggy",
    "great axe",
    "silver bow",
    "spellbook",
    "spiked knuckles",
]

# don't touch above this line

print(f"sword of justice is a top weapon: {'sword of justice' in top_weapons}")
print(f"great axe is a top weapon: {'great axe' in top_weapons}")
print(f"silver bow is a top weapon: {'silver bow' in top_weapons}")

