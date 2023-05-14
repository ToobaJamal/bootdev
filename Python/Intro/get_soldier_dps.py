'''
Your manager has noticed that there's a lot of repetitive code in the "Age of Dragons" code base. 
She has tasked you with reworking the fight_soldiers function so that the DPS (damage-per-second) calculation logic is only written once.
'''

def get_soldier_dps(soldier):
    return soldier["damage"] * soldier["attacks_per_second"]


def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"
