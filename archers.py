'''
Assignment
Complete the Archer class.

Constructor
The constructor should take and set as properties the following parameters in order:

num_arrows
health
name
get_shot method
Create a method called get_shot that doesn't take any parameters.

If the current archer has health left it removes one health from the current archer. 
Then, if the archer's health is 0 it prints the string: {} is dead where {} is the archer's name.

shoot method
Create a method called shoot that takes a target archer as input.

If the shooter has no arrows left, raise the exception {} can't shoot where {} is the archer's name. 
Otherwise, remove an arrow from the shooter and print {1} shoots {2} where {1} is the shooter's name and {2} is the name of the target. 
Next, call the target's get_shot() method.
'''

class Archer:
    def __init__(self, num_arrows, health, name):
        self.num_arrows = num_arrows
        self.health = health
        self.name = name

    def get_shot(self):
        if self.health >= 1:
            self.health -= 1
        else:
            print(f"{self.name} is dead")

    def shoot(self, target):
        if self.num_arrows >= 1:
            self.num_arrows -= 1
            print(f"{self.name} shoots {target.name}")
            target.get_shot()
        else:
            print(f"{self.name} can't shoot")
