import copy

class TicTacToe:
    def __init__(self):
        c = input("Welcome to Tic-Tac-Toe! Which player will be going first, X or O? ")
        c = c.replace(" ", "")
        if not (c == 'X' or c == 'O'):
            c = input("Try again. Which player will be going first, X or O? ")
            c = c.replace(" ", "")
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.turn = 0 #players 0 and 1
        self.piece = c
        self.mainEventLoop()

    def display(self):
        print("The board looks like this:")
        print('''
               {0} | {1} | {2}
              -----------
               {3} | {4} | {5}
              -----------
               {6} | {7} | {8}'''.format(*[i for sublist in self.board for i in sublist]))

    def makeMove(self):
        print("It is currently Player {}'s turn to make a move ({})".format(self.turn+1, self.piece))
        move = int(input('''Where would you like to move? Input your move as one of the following squares.\n
               0 | 1 | 2
              -----------
               3 | 4 | 5
              -----------
               6 | 7 | 8
              '''))
        r,c = move//3, move % 3
        while r < 0 or r > 2 or c < 0 or c > 2 or self.board[r][c] != ' ':
            move = int(input("That square is invalid. Please pick a valid square "))
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

class Game():
    def __init__(self, c = 'X'):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.movesLeft = list(range(9))
        self.turn = 0 #players 0 and 1
        self.piece = c

    def display(self):
        print("The board looks like this:")
        print('''
               {0} | {1} | {2}
              -----------
               {3} | {4} | {5}
              -----------
               {6} | {7} | {8}'''.format(*[i for sublist in self.board for i in sublist])) #flatten list

    def legalMove(self, move):
        if move in self.movesLeft:
            return True
        return False

    def evaluatePosition(self):
        # Rows
        if (self.board[0][0] != ' ' and self.board[0][0] == self.board[0][1] and self.board[0][0] == self.board[0][2]) or \
            (self.board[1][0] != ' ' and self.board[1][0] == self.board[1][1] and self.board[1][0] == self.board[1][2]) or \
            (self.board[2][0] != ' ' and self.board[2][0] == self.board[2][1] and self.board[2][0] == self.board[2][2]):
            return -1
        # Columns
        if (self.board[0][0] != ' ' and self.board[0][0] == self.board[1][0] and self.board[0][0] == self.board[2][0]) or \
            (self.board[0][1] != ' ' and self.board[0][1] == self.board[1][1] and self.board[0][1] == self.board[2][1]) or \
            (self.board[0][2] != ' ' and self.board[0][2] == self.board[1][2] and self.board[0][2] == self.board[2][2]):
            return -1
        # Diagonals
        if (self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]) or \
            (self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]):
            return -1
        if len(self.movesLeft) == 0:
            return 0
        return False

    def makeMove(self, move):
        r,c = move//3, move % 3
        self.board[r][c] = self.piece
        self.movesLeft.remove(move)
        self.turn = (self.turn+1) % 2
        self.piece = 'X' if self.piece == 'O' else 'O'

    def endGame(self):
        if len(self.movesLeft) == 0:
            return True
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

class TicTacToeAI():
    def __init__(self):
        c = input("Welcome to AI Tic-Tac-Toe! Would you like to go first (X) or second (O)? ")
        c = c.replace(" ", "")
        if not (c == 'X' or c == 'O'):
            c = input("Try again. Would you like to go first (X) or second (O)? ")
            c = c.replace(" ", "")
        self.player = c
        game = Game('X')
        self.mainEventLoop(game)

    def display(self, game):
        game.display()

    def makeMove(self, game):
        print("It is currently Player {}'s turn to make a move ({})".format(game.turn+1, game.piece))
        move = int(input('''Where would you like to move? Input your move as one of the following squares.\n
               0 | 1 | 2
              -----------
               3 | 4 | 5
              -----------
               6 | 7 | 8
              '''))
        while not game.legalMove(move):
            move = int(input("That square is invalid. Please pick a valid square "))
        game.makeMove(move)
        return game

    def makeAIMove(self, game):
        move, score = self.minimax(game)
        print("The AI chose move {}. ".format(move))
        game.makeMove(move)
        return game

    def minimax(self, game):
        ''' Returns best action and its value from the current board state. '''
        bestAction, bestScore = -1, -100
        if game.endGame():
            return None, game.evaluatePosition()
        for action in game.movesLeft:
            newGame = Game(game.piece)
            newGame.board = copy.deepcopy(game.board)
            newGame.movesLeft = copy.deepcopy(game.movesLeft)
            newGame.turn = game.turn
            newGame.makeMove(action)
            nextAction, score = self.minimax(newGame)
            score *= -1
            if score > bestScore:
                bestAction, bestScore = action, score
        return bestAction, bestScore

    def mainEventLoop(self, game):
        currentGame = game
            self.display(currentGame)
        while not currentGame.endGame():
            if currentGame.piece == self.player:
                self.makeMove(currentGame)
            else:
                self.makeAIMove(currentGame)
            self.display(currentGame)
        if len(currentGame.movesLeft) == 0:
            print("The game ended in a draw.")
        else:
            winner = ((currentGame.turn+1) % 2) + 1
            print("Congratulations to Player {} for winning!".format(winner))

num = int(input("Welcome to Tic-Tac-Toe! Type in 1 to play a player and 2 to play the AI. "))
while not c == 1 or c == 2:
     num = int(input("Try again. Type in 1 to play a player and 2 to play the AI. "))
if num == 1:
    t = TicTacToe()
else:
    t = TicTacToeAI()
