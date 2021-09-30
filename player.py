
class Player:
    """
    """
    def __init__(self, hp):
        self.hp = hp
        self.speed = 2
        self.inventory = []

    def addToInventory(self, item):
        self.inventory.append(item)

    def printInventory(self):
        if len(self.inventory) <= 0 : print("Your inventory is empty.")
        else:
            print("In your inventory you have: ")
            for item in self.inventory:
                print(item.getName())

    def dropItem(self, item_name):
        for index in range(len(self.inventory)):
            if self.inventory[index].getName().lower() == item_name:
                return self.inventory.pop(index)
        return None

    def getItem(self, item_name):
        for index in range(len(self.inventory)):
            if self.inventory[index].getName().lower() == item_name:
                return self.inventory[index]
        return None

    def getHP(self):
        return self.hp

    def isAlive(self):
        return self.hp > 0

    def getSpeed(self):
        return self.speed

    def hit(self, damage):
        self.hp -= damage
        print(f"You have taken {damage} damage, your hp is now at {self.hp}")
        return damage
