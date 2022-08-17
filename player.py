#tictactoe

#splitting player and game into 2 seperate classes

import math
import random 

class Player:
    #_init_ represents self initialising class
    #this is basically the constructor
    def __init__(self , letter):
        #letter is either x or o
        self.letter = letter

    def get_move(self,game):
        pass

    

#here we are using inheritance, inheriting properties from the Player class
class RandomComputerPlayer(Player):
    #in inheritance, we have to initialise superclass which is below
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square
#tip: use super() whenevr you use inheritance - for ease of coding

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False #we want the user to keep choosing a spot until it's fine, hence we have put it false as default
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ' )
            #checking if the input value is correct and valid by trying
            #to cast it to an integer. If it's not, we say it's invalid
            #And if the spot isn't avaliable, we say it's invalid as well
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #set it to be True if it's valid!

            except ValueError:
                print("Invalid. Try again")

        return val