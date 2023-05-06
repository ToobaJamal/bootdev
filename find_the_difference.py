'''
We keep track of each character's level in an array. 
When someone's level changes we want to know about it so we can congratulate them! 
Your assignment is to find any differences between the old_character_levels and new_character_levels lists, 
and to print the index where the values are different.

The shell of the loop you've been given loops over all of the indexes in old_character_levels. 
Because old_character_levels and new_character_levels are the same lengths, you can reuse i to index into both.
'''

old_character_levels = [ 6, 4, 3, 7, 7, 7, 2, 7, 2, 6, 5, 1, 2, 4, 6, 6, 1, 4, 4, 1, 1, 5, 4, 3, 2, 0, 5, 5, 6, 1, 6, 2, 1, 2, 3, 1, 7, 7, 2, 0, 0, 6, 2, 6, 8, 5, 3, 1, 6, 3, 0, 5, 1, 3, 3, 0, 2, 8, 3, 0, 3, 5, 7, 3, 1, 4, 5, 0, 0, 1, 7, 0, 6, 1, 0, 2, 0, 0, 8, 6, 0, 0, 1, 4, 0, 7, 8, 2, 7, 8, 7, 4, 8, 6, 0, 3, 1, 4, 6, 4, 2, 2, 5, 8, 1, 5, 1, 8, 0, 6, 6, 3, 0, 2, 4, 7, 0, 6, 7, 6, 3, 1, 1, 5, 2 ]
new_character_levels = [ 6, 4, 3, 7, 7, 7, 2, 7, 2, 6, 5, 1, 2, 4, 5, 6, 1, 4, 4, 1, 1, 5, 4, 3, 2, 1, 2, 5, 6, 1, 6, 2, 1, 2, 3, 1, 7, 7, 2, 0, 0, 6, 2, 6, 8, 5, 3, 1, 6, 3, 0, 5, 1, 3, 3, 0, 2, 8, 3, 0, 3, 5, 7, 3, 1, 4, 5, 0, 0, 1, 7, 0, 6, 1, 0, 2, 0, 0, 8, 6, 0, 0, 1, 4, 0, 7, 8, 2, 7, 8, 7, 4, 9, 6, 0, 3, 3, 4, 6, 4, 2, 2, 5, 8, 1, 5, 1, 8, 0, 6, 6, 3, 0, 2, 4, 7, 0, 6, 7, 6, 3, 1, 8, 5, 2 ]

# don't touch above this line

for i in range(0, len(old_character_levels)):
    if old_character_levels[i] < new_character_levels[i]:
        print(i)
