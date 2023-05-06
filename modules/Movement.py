from modules.Validation import Validate
#from modules.Board import Board
from modules.Constants import *

def movePiece(self, event):
        # Get the current position of the mouse
        self.x = event.x-(SQSIZE/2)
        self.y = event.y-(SQSIZE/2)
        self.x = 0 if self.x < 0 else self.x
        self.y = 0 if self.y < 0 else self.y
        self.x = 525 if self.x > 525 else self.x
        self.y = 525 if self.y > 525 else self.y
        # Move the image to the new position
        self.board.coords(self.button_id, self.x, self.y)
        self.board.lift(self.button_id)

def startMovement(self, event):
    from modules.Board import Board
    self.x, self.y = event.x, event.y
    moves, kills = Validate.getPossibleMoves(self.pos,self.piece, self.colour,self.moved,Board.boardArr)
    print(kills)
    self.validMoves = moves
    self.validKills = kills
    #Note this colour down for the movement: FFDD80. It shows the last move.
    # And for valid moves: 80FF67
    if moves != []:
        for pos in moves:
            self.imageIDs.append(Board.showMove(pos,self.board))
    if kills != []:
        for pos in kills:
            self.imageIDs.append(Board.showKill(pos,self.board))


def stopMovement(self, event):
    from modules.Pieces import Piece
    from modules.Board import Board

    def move(x, y, moved):
        board.coords(self.button_id, x*75, y*75)
        for id in self.imageIDs:
            board.delete(id)
        if moved:
            Board.boardArr[y][x] = Board.boardArr[self.pos[0]][self.pos[1]]
            Board.boardArr[self.pos[0]][self.pos[1]] = Piece(board, 0, self.pos, self.colour)
            print(Board.boardArr[y][x].piece)
            self.pos = [y, x]
            for i in Board.boardArr:
                for j in i:
                    if j.piece == 2:
                        j.enPassantValid = False
            if self.piece == 2:
                self.enPassantValid = Validate.checkEnPassantValid(self.colour, self.pos, Board.boardArr)
        
    x = event.x//75
    y = event.y//75
    XOutsideLimits = self.x == 0 or self.x == 525
    YOutsideLimits = self.y == 0 or self.y == 525
    board = self.board
    board.lift(self.button_id)
    if Board.boardArr[y][x].piece != 0:
        move(self.pos[1], self.pos[0], False)
    elif [y, x] not in self.validMoves:
        move(self.pos[1], self.pos[0], False)
    elif XOutsideLimits:
        x = self.x//75
        if YOutsideLimits:
            y = self.y//75
        move(x, y, True)
        self.firstMove = False
        self.moved = True
    elif YOutsideLimits:
        y = self.y//75
        move(x, y, True)
        self.firstMove = False
        self.moved = True
    else:
        move(x, y, True)
        self.firstMove = False
        self.moved = True
