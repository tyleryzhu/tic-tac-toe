class TicTacToe:
    def __init__(self):
        c = input("Welcome to Tic-Tac-Toe! Which player will be going first, X or O?")
        if not (c == 'X' or c == 'O'):
            c = input("Try again. Which player will be going first, X or O?")
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.turn = 0 #players 0 and 1
        self.piece = c
        self.mainEventLoop()
    
    def display(self):
        print("It is currently Player {}'s turn to make a move ({})".format(self.turn+1, self.piece))
        print("The board looks like this:")
        print(''' 
               {0} | {1} | {2} 
              -----------
               {3} | {4} | {5}
              -----------
               {6} | {7} | {8}
              '''.format(*[i for sublist in self.board for i in sublist]))
    
    def makeMove(self):
        move = int(input('''Where would you like to move? Input your move as one of the following squares.\n
               0 | 1 | 2 
              -----------
               3 | 4 | 5
              -----------
               6 | 7 | 8
              '''))
        r,c = move//3, move % 3
        while r < 0 or r > 2 or c < 0 or c > 2 or self.board[r][c] != ' ':
            move = int(input("That square is invalid. Please pick a valid square"))
            r,c = move//3, move % 3
        self.board[r][c] = self.piece
        self.turn = (self.turn+1) % 2
        self.piece = 'X' if self.piece == 'O' else 'O'
    
    def endGame(self):
        # Rows 
        if (self.board[0][0] != ' ' and self.board[0][0] == self.board[0][1] and self.board[0][0] == self.board[0][2]) or \
            (self.board[1][0] != ' ' and self.board[1][0] == self.board[1][1] and self.board[1][0] == self.board[1][2]) or \
            (self.board[2][0] != ' ' and self.board[2][0] == self.board[2][1] and self.board[2][0] == self.board[2][2]):
            return True
        # Columns
        if (self.board[0][0] != ' ' and self.board[0][0] == self.board[1][0] and self.board[0][0] == self.board[2][0]) or \
            (self.board[0][1] != ' ' and self.board[0][1] == self.board[1][1] and self.board[0][1] == self.board[2][1]) or \
            (self.board[0][2] != ' ' and self.board[0][2] == self.board[1][2] and self.board[0][2] == self.board[2][2]): 
            return True
        # Diagonals
        if (self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]) or \
            (self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]):
            return True
        return False
    
    def mainEventLoop(self):
        while not self.endGame():
            self.display()
            self.makeMove()
        self.display()
        winner = ((self.turn+1) % 2) + 1
        print("Congratulations to Player {} for winning!".format(winner))

t = TicTacToe()