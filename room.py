from __future__ import annotations
import item
import random

class Room :
    def __init__(self, name) :
        self.name = name
        self.items = []

    def addItem(self, item: item.Item):
        self.items.append(item)

    def getItems(self):
        return self.items

    def takeItem(self, item_name):
        for index in range(len(self.items)):
            if self.items[index].getName().lower() == item_name:
                return self.items.pop(index)
        return None


    def getName(self) :
        return self.name
    
    def printRoomInfo(self):
        print(f"You are in a {self.name}.")
        if len(self.items) > 0:
            for i in self.items:
                print(f"You see a {i.getName()}.")


def generateRoom():
    i = random.randint(0, 3)
    room = None
    if i == 0: room = Room("Forest")
    elif i == 1: room = Room("Canyon")
    elif i == 2: room = Room("Plains")
    elif i == 3: room = Room("Swamp")
    
    i = random.randint(0, 3)
    if i == 0:
        thing = item.getRandomItem()
        room.addItem(thing)

    return room