from map import Map
from player import Player
from fight import Fight
import enemy
import item
from random import randint

def help():
    ''' Displays the commands avaliable when running the game '''
    print("Commands avaliable: ")
    print("go - Move in the given direction (North, West, South or East).")
    print("inventory - Prints a list of all your stuffs.")
    print("take - Tries to take an item from the ground and place it in your inventory.")
    print("drop - Tries to drop an item from your inventory on the ground.")
    print("look - You look around and see any item visible in the area.")
    print("help - Displays this message.")
    print("quit - Exits the game.")

def getUserCommands():
    ''' Returns an array of the commands the user is promted to input '''
    command = input("What do you wish to do? ").lower().lstrip()
    return command.split(" ")


class Game:
    ''' The game class runs the game one turn at a time  '''
    def __init__(self):
        self.__keepPlaying = True
        self.player = Player(20)
        self.player.addToInventory(item.getRandomItem())
        self.map = Map()
        self.last_command = ""

    def keepPlaying(self):
        ''' Returns true when the game is still running and the player is alive '''
        return self.__keepPlaying and self.player.isAlive()

    def setup(self):
        ''' Prints the status of the player '''
        print(f"Player HP: {self.player.getHP()}")
        self.player.printInventory()

    def encounterEnemy(self, direction):
        ''' Has a one in 3 chance of starting a fight with a random enemy '''
        if randint(0, 2) == 0:
            foe = enemy.getRandomEnemy()
            print(f"On your travels {direction} you encounter a {foe.getName()}")
            fight = Fight(self.player, foe)
            fight.start()

    def movePlayer(self, direction):
        ''' Moves player in the direction of choice and may cause an encounter with an enemy ''' 
        if direction == "north": 
            self.map.goNorth()
            self.encounterEnemy("north")
        elif direction == "south": 
            self.map.goSouth()
            self.encounterEnemy("south")
        elif direction == "west": 
            self.map.goWest()
            self.encounterEnemy("west")
        elif direction == "east": 
            self.map.goEast()
            self.encounterEnemy("east")
        else: print("That is not a direction i am familiar with.")

    def take(self, arg):
        ''' Tries to take an item from the current room and place it in the player inventory'''
        thing = self.map.getCurrentRoom().takeItem(arg)
        if thing == None: print("Could not find that item")
        else:
            self.player.addToInventory(thing)
            print("Taken.")
        
    def drop(self, arg):
        ''' Tries to take an item from the player inventory and place it in the current room '''
        thing = self.player.dropItem(arg)
        if thing == None: print("You have no such thing in your inventory.")
        else:
            self.map.getCurrentRoom().addItem(thing)
            print("Dropped")

    def look(self):
        ''' Displays information about the current room, and what items you can see '''
        self.map.getCurrentRoom().printRoomInfo()

    def quit(self):
        ''' Stops the game from running '''
        self.__keepPlaying = False

    def nextRound(self):
        ''' Performs the next round, prompting and executing a command from the user '''        
        print("-----------")
        if self.last_command == "go" : self.look()
        else: print(self.map.getCurrentRoom().getName())

        commands = getUserCommands()
        if commands[0] == "go": self.movePlayer(commands[1])
        elif commands[0] == "inventory": self.player.printInventory()
        elif commands[0] == "take": self.take(commands[1])
        elif commands[0] == "drop": self.drop(commands[1])
        elif commands[0] == "look": self.look()
        elif commands[0] == "help": help()
        elif commands[0] == "quit": self.quit()
        else: print("You cannot do that.")
        
        self.last_command = commands[0]
