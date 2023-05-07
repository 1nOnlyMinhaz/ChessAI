from modules.Validation import *
from modules.Constants import *

def movePiece(self, event):
        # Get the current position of the mouse
        self.x = event.x-(SQSIZE/2)
        self.y = event.y-(SQSIZE/2)
        self.x = 0 if self.x < 0 else self.x
        self.y = 0 if self.y < 0 else self.y
        self.x = MAXPIECEX if self.x > MAXPIECEX else self.x
        self.y = MAXPIECEY if self.y > MAXPIECEY else self.y
        # Move the image to the new position
        self.board.coords(self.button_id, self.x, self.y)
        self.board.lift(self.button_id)

def startMovement(self, event):
    from modules.Board import Board
    self.x, self.y = event.x, event.y
    moves = ValidateMoves.getPossibleMoves(self.pos,self.piece, self.colour,self.moved,Board.boardArr)
    kills = ValidateKills.getPossibleKills(self.pos,self.piece, self.colour,self.moved,Board.boardArr)
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
    from modules.Kill import Kill
    def move(x, y, moved):
        board.coords(self.button_id, x*SQSIZE, y*SQSIZE)
        for id in self.imageIDs:
            board.delete(id)
        if moved:
            Board.boardArr[y][x] = Board.boardArr[self.pos[0]][self.pos[1]]
            Board.boardArr[self.pos[0]][self.pos[1]] = Piece(board, 0, self.pos, "None")
            print(Board.boardArr[self.pos[0]][self.pos[1]].piece)
            self.pos = [y, x]
            for i in Board.boardArr:
                for j in i:
                    if j.piece == Piece.Pawn:
                        j.enPassantValid = False
            if self.piece == Piece.Pawn:
                self.enPassantValid = ValidateMoves.checkEnPassantValid(self.colour, self.pos, Board.boardArr)
        
    x = event.x//SQSIZE
    y = event.y//SQSIZE
    XOutsideLimits = self.x == 0 or self.x == MAXPIECEX
    YOutsideLimits = self.y == 0 or self.y == MAXPIECEY
    if XOutsideLimits:
        x = self.x//SQSIZE
    if YOutsideLimits:
        y = self.y//SQSIZE
    board = self.board
    board.lift(self.button_id)
    if [y, x] in self.validKills:
        Kill(board, [y, x], self.colour)
        move(x, y, True)
        self.firstMove = False
        self.moved = True
    elif Board.boardArr[y][x].piece != 0:
        move(self.pos[1], self.pos[0], False)
    elif [y, x] not in self.validMoves:
        move(self.pos[1], self.pos[0], False)
    else:
        move(x, y, True)
        self.firstMove = False
        self.moved = True
