'''
Due to our terrible class design, some lazy code owned by a different development team is causing some bugs in our class. 
We can fix it by using instance variables instead of class variables.

In the main() function (that our team isn't responsible for), a line like Dragon.element = "fire" should not affect our existing dragon instances! 
We don't like near-global variables. We want our users to specify each dragon's element in the constructor.

Update the Dragon class. Remove the element class variable and instead use an instance variable that's configurable via the constructor.
'''

class Dragon:
    def __init__(self, element):
        self.element = element

    def get_breath_damage(self):
        if self.element == "fire":
            return 300
        if self.element == "ice":
            return 150
        return 0


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    first_dragon = Dragon("fire")
  
    print(
        f"{first_dragon.element} dragon does {first_dragon.get_breath_damage()} damage"
    )

    second_dragon = Dragon("ice")
    Dragon.element = "fire"
    print(
        f"{second_dragon.element} dragon does {second_dragon.get_breath_damage()} damage"
    )


main()
