'''
We need to be able to report to our players how many enemies are in their immediate vicinity - but they want the count of each enemy by its kind. 
Complete the count_enemies function. It takes a list of enemy names as input. 
It should return a dictionary where the keys are all the enemy names from the list, 
and the values are the counts of how many times each enemy appeared in the list.
'''

def count_enemies(enemy_names):
    count_dictionary = {}
    for i in enemy_names:
        if(i in count_dictionary):
            count_dictionary[i] = count_dictionary[i]+1
        else:
            count_dictionary[i] = 1
    return count_dictionary


# Don't edit below this line


def main():
    print(
        count_enemies(
            [
                "jackal",
                "kobold",
                "jackal",
                "kobold",
                "soldier",
                "kobold",
                "soldier",
                "soldier",
                "jackal",
                "jackal",
                "gremlin",
                "jackal",
                "jackal",
            ]
        )
    )


main()
