import random

class Item:

    def __init__(self, name, hardness):
        self.name = name
        self.hardness = hardness

    def getName(self):
        return self.name

    def getHardness(self):
        return self.hardness

    def use(self):
        return None

class Sword(Item):
    def __init__(self):
        super().__init__("Sword", 5)

class Knife(Item):
    def __init__(self):
        super().__init__("Knife", 4)

class Bottle(Item):
    def __init__(self):
        super().__init__("Bottle", 2)


def getRandomItem():
    i = random.randint(0, 2)
    if i == 0: return Sword()
    elif i == 1: return Knife()
    elif i == 2: return Bottle()
    else: return Item("Flower", 0)