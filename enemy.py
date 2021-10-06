from random import randint

class Enemy:
    ''' All enemies has a name, some hitpoints, strength and speed '''
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.speed = 0 

    def getName(self):
        ''' Get the name of the enemy '''
        return self.name

    def getHP(self):
        ''' Returns the current hp of the enemy '''
        return self.hp

    def getStrength(self):
        ''' Returns the strength of the enemy '''
        return self.strength

    def getSpeed(self):
        ''' Returns the speed of the enemy '''
        return self.speed

    def isAlive(self):
        ''' Returns true if the enemy is alive, ie. has hp left '''
        return self.hp > 0

    def hit(self, damage):
        ''' Loses hitpoints and returns how much the damage affected the enemy '''
        self.hp -= damage
        return damage

class Troll(Enemy):
    ''' A Troll is a type of enemy, it may be slow but it is powerful '''
    def __init__(self, hp, strength):
        super().__init__("Troll", hp, strength)
        self.speed = 1

    def hit(self, damage):
        ''' Trolls only take half as much damage from hits '''
        self.hp -= damage/2
        return damage/2

    def randomize():
        ''' Generates a new random troll '''
        hp = randint(3, 7)
        strength = randint(2, 3)
        return Troll(hp, strength)

class Goblin(Enemy):
    ''' Goblins are weak but fast anoying enemies '''
    def __init__(self, hp, strength):
        super().__init__("Goblin", hp, strength)
        self.speed = 3

    def randomize():
        ''' Generates a new random Goblin '''
        hp = randint(1, 4)
        strength = randint(1, 2)
        return Goblin(hp, strength)
        
class Snail(Enemy):
    ''' Snails may not seen to be enemeies at all, yet they seem to obstruct our path '''
    def __init__(self):
        super().__init__("Snail", 1, 0)

def getRandomEnemy():
    ''' Generate a random enemy '''
    i = randint(0, 3)
    if i == 0: return Troll.randomize()
    elif i == 1: return Goblin.randomize()
    else: return Snail()