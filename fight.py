from random import randint
from player import Player
from enemy import Enemy


class Fight:
    ''' A Fight is an object containing the loop and logic for what happens in a battle between a player and a enemy '''
    def __init__(self, player:Player, foe:Enemy):
        self.player = player
        self.foe = foe
        self.inBattle = True

    def isFighting(self):
        ''' Returns true while still in battle, ie. when both player and enemy is alive and the player has not yet succeded in fleeing '''
        return self.player.isAlive() and self.foe.isAlive() and self.inBattle

    def useItem(self, item_name):
        ''' Tries to use an item to fight the enemy '''
        thing = self.player.getItem(item_name)
        if thing == None:
            print("Could not find any item with that name")
        else:
            if randint(0,2) == 0:
                damage = self.foe.hit(thing.getHardness())
                print(f"You hit the {self.foe.getName()} with a {thing.getName()} dealing {damage} damage.")
            else: print(f"You failed to hit the {self.foe.getName()} with the {thing.getName()}!")

    def punch(self):
        ''' Tries to punch enemy ''' 
        damage = randint(0, 2)
        if damage > 0:
            damage = self.foe.hit(damage)
            print(f"You hit the {self.foe.getName()}, dealing {damage} damage to it.")
        else: print(f"You were too weak to punch the {self.foe.getName()}.")

    def kick(self):
        ''' Tries to kick enemy '''
        damage = randint(0, 2)
        if damage > 0:
            damage = self.foe.hit(damage)
            print(f"You kick the {self.foe.getName()}, dealing {damage} damage to it.")
        else: print(f"You failed trying to kick the {self.foe.getName()}.")

    def escape(self):
        ''' Player tries to escape from enemy '''
        if self.player.getSpeed() >= self.foe.getSpeed():
            diff = (self.player.getSpeed() - self.foe.getSpeed())+1
            if randint(0, diff) >= 1:
                self.inBattle = False
                print(f"You managed to escape from the {self.foe.getName()}, it ran away.")
                return
        print(f"You failed to escape from the {self.foe.getName()}, it is too fast.")

    def playerTurn(self):
        ''' Displays the enemys hp and offers the player a choice on what to do '''
        print("--------")
        print(f"The {self.foe.getName()} has {self.foe.getHP()} hp left:")
        
        commands = input(f"How do you wish to fight the {self.foe.getName()}? ").lower().lstrip().split(" ")
        if commands[0] == "use":self.useItem(commands[1])
        elif commands[0] == "punch": self.punch()
        elif commands[0] == "kick": self.kick()
        elif commands[0] == "escape": self.escape()
        else: print("Trying to do the impossible, you failed to do any damage.")

    def enemyTurn(self):
        ''' The enemys action '''
        if self.isFighting(): # enemy attacks
            damage = randint(0, self.foe.getStrength())
            if damage > 0 :print(f"The {self.foe.getName()} attacks you with is fists and deal {damage} damage to you!")
            else: print(f"The {self.foe.getName()} tries to attack you, but you deflect his attack!")
            self.player.hit(damage)
        elif not self.inBattle: print("You continue on your journey.") 
        else: print(f"\nThe {self.foe.getName()} died trying to get home.")

    def start(self):
        ''' Starts the battle and loops until the fight is over ''' 
        while self.isFighting():
            self.playerTurn()
            self.enemyTurn()