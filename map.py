import room

# 
#   Generate rooms for all positions needed, when needed
#
#
class Map:
    ''' The map contans all the rooms the player has visited '''
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.tiles = {}
        self.__createIfNotExists()
    
    def goNorth(self):
        ''' moves position North and generates a room if there is`nt one '''
        self.pos_y += 1
        self.__createIfNotExists()

    def goSouth(self):
        ''' moves position South and generates a room if there is`nt one '''
        self.pos_y -= 1
        self.__createIfNotExists()

    def goWest(self):
        ''' moves position West and generates a room if there is`nt one '''
        self.pos_x -= 1
        self.__createIfNotExists()

    def goEast(self):
        ''' moves position East and generates a room if there is`nt one '''
        self.pos_x += 1
        self.__createIfNotExists()

    def __createIfNotExists(self):
        ''' Generates a room for the current position if there is`nt one already generated '''
        if (f"{self.pos_x} : {self.pos_y}") not in self.tiles:
            self.tiles[f"{self.pos_x} : {self.pos_y}"] = room.generateRoom()
        

    def getCurrentRoom(self):
        ''' Returns the room object of the current position '''
        return self.tiles[f"{self.pos_x} : {self.pos_y}"]