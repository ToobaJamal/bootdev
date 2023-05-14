'''
In Fantasy Quest there are a list of strongholds on the map that players can visit to defeat powerful bosses.

Delete the first stronghold from the list
Print the list of strongholds
Delete the last two strongholds from the list as a slice
Print the list of strongholds
'''

strongholds = [
    "Rivendale",
    "The Morgoth Mountains",
    "The Lonely Island",
    "Mordia",
    "Mordane",
    "Gondolin",
]

# Don't touch above this line

del strongholds[0]
print(strongholds)
del strongholds[3:]
print(strongholds)

