class TicTacToe:
    def __init__(self):
        self.board = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
        ]
        self.turn = "x"
        self.other = "o"
    
    def place(self, x, y):
        self.board[x][y] = self.turn
        turn = self.turn
        self.turn = self.other
        self.other = turn
        return "{0} помещен в клетку {1} {2}".format(turn, x, y)
    
    def get(self, x, y):
        return self.board[x][y]

    def is_empty(self, x, y):
        return self.board[x][y] == '_'

    def is_win(self, symbol):
        for row in range(3):
            xs = 0
            for col in range(3):
                if self.board[row][col] == symbol:
                    xs += 1
            if xs == 3:
                return True

        for col in range(3):
            xs = 0
            for row in range(3):        
                if self.board[row][col] == symbol:
                    xs += 1
            if xs == 3:
                return True
        
        left = 0
        right = 0
        x = 2
        y = 0
        for i in range(3):
            if self.board[i][i] == symbol:
                left += 1
            if self.board[x][y] == 'x':
                right += 1
            x -= 1
            y += 1
        if left == 3 or right == 3:
            return True
        else:
            return False

    def empty_board(self):
        for i in self.board:
            for j in self.board[i]:
                self.board[i][j] = "_"

