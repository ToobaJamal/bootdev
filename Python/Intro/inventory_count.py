'''
Our players need a way to see how many copies of a specific item they have within their inventory!

Within the loop, count how many times Potion, Bread, and Shortsword appear using the potion_count, bread_count and shortsword_count variables respectively.
'''

items = [ "Potion", "Iron Breastplate", "Leather Scraps", "Iron Ore", "Light Leather", "Bread", "Shortsword", "Longsword", "Iron Mace", "Gold Ore", "Bread", "Silk Cloth", "Bread",  "Leather Armor Kit", "Bread", "Iron Boots", "Iron Bar", "Potion", "Iron Breastplate", "Leather Scraps", "Iron Ore", "Light Leather", "Bread", "Shortsword", "Longsword", "Iron Mace", "Gold Ore", "Silk Cloth", "Leather Armor Kit", "Iron Boots", "Iron Bar", "Iron Mace", "Gold Ore", "Potion", "Silk Cloth", "Leather Armor Kit", "Iron Boots", "Iron Bar", "Potion", "Iron Breastplate", "Leather Scraps", "Iron Ore", "Light Leather", "Potion", "Iron Breastplate", "Leather Scraps", "Iron Ore", "Light Leather", "Bread", "Shortsword", "Longsword", "Iron Mace", "Gold Ore", "Silk Cloth", "Leather Armor Kit", "Iron Boots", "Iron Bar" ]

potion_count = 0
bread_count = 0
shortsword_count = 0

# don't touch above this line

for i in range(0, len(items)):
    if(items[i] == "Potion"):
        potion_count += 1
    elif(items[i] == "Bread"):
        bread_count += 1
    elif(items[i] == "Shortsword"):
        shortsword_count += 1

# don't touch below this line

print(f"You have {potion_count} potions in your inventory.")
print(f"You have {bread_count} pieces of bread in your inventory.")
print(f"You have {shortsword_count} shortswords in your inventory.")
