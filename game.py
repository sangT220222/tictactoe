import time
from operator import truediv
from player import HumanPlayer,RandomComputerPlayer

class ticTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] ##represents the 3x3 board
        self.current_winner = None #keep track of the winner
    
    def draw_board(self):
        #arr[ start : stop : step ]
        # i will have the values 0,1,2 - therefore resulting in 
        #[0:3] = represents indices 0,1,2 which is our 1st row 
        #[3:6] = represents indices 3,4,5 which is our 2nd row 
        #[6:9] = represents indices 6,7,8 which is our 3rd row 
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod #this means we don't need to pass in any "self"
    def print_board_numbers():
        #0 | 1 | 2 (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    #logic of the game
    def available_moves(self):
        #return []
        #moves = []
        #for i,spot in enumerate(self.board):
            #as enumerate loops through using index and element, 
            #for eg if we have ['x', 'o', 'x'] in our board array
            #this loop will output (0,'x') , (1,'o'), (2, 'x')
        #    if spot == ' ':
        #        moves.append(i)
        #return moves
        ##using list comprehension to simplify the line 24 to 32
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        #note the i for i already compromise the "moves.append(i)" line

    def empty_squares(self):
        #returns a boolean value
        return ' ' in self.board
    
    def num_empty_squares(self):
        #we use count here as board is a list
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move, then make the move (assign square to letter)
        #then return true. else return false
        if self.board[square] ==  ' ':
            self.board[square] = letter
            #assinging the winner to one of the letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    #function to check for a winner
    def winner(self, square, letter):
        #winner if 3 in a row
        #gotto check all rows and diagonals
        row_index = square // 3 # "//" divides the number first and rounds it down to nearest whole number
        row = self.board[row_index*3 : (row_index+1)*3] #list of items in the row we have selected
        if all([spot == letter for spot in row]): #checking if the letter are all in the spot 3 in a row
            return True

        #check column
        col_index = square % 3 #will always be either 0,1,2 
        column = [self.board[col_index + i*3] for i in range(3)] #list of items in the column we have selected
        if all([spot == letter for spot in column]): #checking if the letter are all in the spot 3 in a column
            return True    

        #check diagonal
        #check if the square is an even number as these are the only spots that enable us to win diagonally

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]): #checking if the letter are all in the spot 3 in a diagonal1
                return True
            diagonal2 = [self.board[j] for j in [2,4,6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]): #checking if the letter are all in the spot 3 in diagonal2
                return True
            
        return False   

    def menu(self, user_input):
        if user_input == "0":
            return 0
        elif user_input == "1":
            return 1
        elif user_input == "2":
            return 2
        else:
            print("Invalid input")

  

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_numbers()
    letter = 'X' #starting letter
    # iterate while the game still has empty squares
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #defining a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}.')
                game.draw_board()
                print('')
    
            if game.current_winner:
                if print_game:
                    print(letter + ' wins')
                return letter

            #after move has been made, we need to alternate the letter
            letter = 'O' if letter == 'X' else 'X'

        #tiny pause
        #making sure there is a slight pause between computer's move and printing the board after computer has made its move
        time.sleep(0.9)

    if print_game:
        print('It\'s a tie')
    


if __name__ == '__main__':
    user_score = 0
    cpu_score = 0
    tie_score = 0
    while True: 
        x_player = HumanPlayer('X') #initialising the players
        o_player = RandomComputerPlayer('O')
        t = ticTacToe()
        user_input = str(input("Press 0 to play, 1 for the scores and 2 to quit: "))
        answer = t.menu(user_input)
        if answer == 0 :
             p = play(t , x_player, o_player, print_game = True)
             p
             if p == "X":
                 user_score += 1
             elif p == "O":
                cpu_score += 1
             else:
                tie_score += 1
        elif answer == 1:
            print("User score:" + str (user_score))
            print("CPU score: " + str(cpu_score))
            print("Draws: " + str(tie_score))

        elif answer == 2:
            break



    