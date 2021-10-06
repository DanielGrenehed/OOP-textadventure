from __future__ import annotations
import item
import random

class Room :
    ''' A room or place that has a name and can contain items '''
    def __init__(self, name) :
        self.name = name
        self.items = []

    def addItem(self, item: item.Item):
        ''' Add provided item to room ''' 
        self.items.append(item)

    def getItems(self):
        ''' Returns an array of items that are in the room '''
        return self.items

    def takeItem(self, item_name):
        ''' Removes and returns item with the given name from room if found '''
        for index in range(len(self.items)):
            if self.items[index].getName().lower() == item_name:
                return self.items.pop(index)
        return None


    def getName(self):
        ''' Returns the name of the room '''        
        return self.name
    
    def printRoomInfo(self):
        ''' Prints that you are in the room and all items that are in this room '''
        print(f"You are in a {self.name}.")
        if len(self.items) > 0:
            for i in self.items:
                print(f"You see a {i.getName()}.")


def generateRoom():
    ''' Generate a room with a name and mabey some items ''' 
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