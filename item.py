import random

class Item:
    ''' Items have names and hardness, since all you can do with an item is attack somebody there is no reason to add more features to items '''
    def __init__(self, name, hardness):
        self.name = name
        self.hardness = hardness

    def getName(self):
        ''' Returns the name of the item '''
        return self.name

    def getHardness(self):
        ''' Returns the hardness of the item '''
        return self.hardness


class Sword(Item):
    ''' Swords are hard items '''
    def __init__(self):
        super().__init__("Sword", 5)

class Knife(Item):
    ''' Knifes are less powerful than swords '''
    def __init__(self):
        super().__init__("Knife", 4)

class Bottle(Item):
    ''' Bottles are terrible weapons '''
    def __init__(self):
        super().__init__("Bottle", 2)


def getRandomItem():
    ''' Generates a random item '''
    i = random.randint(0, 2)
    if i == 0: return Sword()
    elif i == 1: return Knife()
    elif i == 2: return Bottle()
    else: return Item("Flower", 0)