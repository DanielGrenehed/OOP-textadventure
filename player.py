
class Player:
    ''' A player is the character of the user in game, he has hp, a set speed and an inventory '''
    def __init__(self, hp):
        self.hp = hp
        self.speed = 2
        self.inventory = []

    def addToInventory(self, item):
        ''' Adds an item to the player inventory '''
        self.inventory.append(item)

    def printInventory(self):
        ''' Prints what items there are in the player inventory ''' 
        if len(self.inventory) <= 0 : print("Your inventory is empty.")
        else:
            print("In your inventory you have: ")
            for item in self.inventory:
                print(item.getName())

    def dropItem(self, item_name):
        ''' Removes and returns item with given name from inventory if found '''
        for index in range(len(self.inventory)):
            if self.inventory[index].getName().lower() == item_name:
                return self.inventory.pop(index)
        return None

    def getItem(self, item_name):
        ''' Returns an item with the given name if it is found in inventory '''
        for index in range(len(self.inventory)):
            if self.inventory[index].getName().lower() == item_name:
                return self.inventory[index]
        return None

    def getHP(self):
        ''' Returns the current hp of the player '''
        return self.hp

    def isAlive(self):
        ''' Returns true if player still have hp above o '''
        return self.hp > 0

    def getSpeed(self):
        ''' Returns the speed of the player '''
        return self.speed

    def hit(self, damage):
        ''' damages player and returns how much damage taken '''
        self.hp -= damage
        print(f"You have taken {damage} damage, your hp is now at {self.hp}")
        return damage
