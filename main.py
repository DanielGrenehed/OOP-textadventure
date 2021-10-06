from game import Game

if __name__ == "__main__":
    ''' This is where the actual game is started, and where the game loop resides '''
    game = Game()
    game.setup()

    while game.keepPlaying(): game.nextRound()
        
    if game.player.isAlive(): print("You have quit the game!")
    else: print("You have taken too much damage, you are now dead.")


