
import room

# 
#   Generate rooms for all positions needed, when needed
#
#
class Map:

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.tiles = {}
        self.__createIfNotExists()
    
    def goNorth(self):
        self.pos_y += 1
        self.__createIfNotExists()

    def goSouth(self):
        self.pos_y -= 1
        self.__createIfNotExists()

    def goWest(self):
        self.pos_x -= 1
        self.__createIfNotExists()

    def goEast(self):
        self.pos_x += 1
        self.__createIfNotExists()

    def __createIfNotExists(self):
        if (f"{self.pos_x} : {self.pos_y}") not in self.tiles:
            self.tiles[f"{self.pos_x} : {self.pos_y}"] = room.generateRoom()
        

    def getCurrentRoom(self):
        return self.tiles[f"{self.pos_x} : {self.pos_y}"]