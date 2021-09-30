from random import randint

class Enemy:

    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.speed = 0 

    def getName(self):
        return self.name

    def getHP(self):
        return self.hp

    def getStrength(self):
        return self.strength

    def getSpeed(self):
        return self.speed

    def isAlive(self):
        return self.hp > 0

    def hit(self, damage):
        self.hp -= damage
        return damage

class Troll(Enemy):
    def __init__(self, hp, strength):
        super().__init__("Troll", hp, strength)
        self.speed = 1

    def hit(self, damage):
        self.hp -= damage/2
        return damage/2

    def randomize():
        hp = randint(3, 7)
        strength = randint(2, 3)
        return Troll(hp, strength)

class Goblin(Enemy):
    def __init__(self, hp, strength):
        super().__init__("Goblin", hp, strength)
        self.speed = 3

    def randomize():
        hp = randint(1, 4)
        strength = randint(1, 2)
        return Goblin(hp, strength)
        
class Snail(Enemy):
    def __init__(self):
        super().__init__("Snail", 1, 0)

def getRandomEnemy():
    i = randint(0, 3)
    if i == 0: return Troll.randomize()
    elif i == 1: return Goblin.randomize()
    else: return Snail()