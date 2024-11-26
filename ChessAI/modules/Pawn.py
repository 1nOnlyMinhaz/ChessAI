from modules.Pieces import Piece
from modules.Promotion import Promotion

class Pawn(Piece):
    def __init__(self, board, color, position):
        super().__init__(board, "Pawn", color, position)
        self.board = board
        self.color = color
        self.pos = position
        self.hasMoved = False
        self.enPassantPositions = []

    def startMovement(self, event):
        x = self.pos[0]
        y = self.pos[1]
        if self.color != self.board.CurrentColour:
            return
        if len(self.enPassantPositions) != 0:
            self.killImages.append(self.board.createImage("./kill.png", self.validKills[-1], "Kill"))
        if self.color == "White":
            if y-1 >= 0:
                if self.board.pieces[y-1][x] == 0:
                    self.validMoves.append([x, y-1])
                    self.moveImages.append(self.board.createImage("./move.png", self.validMoves[0], "Move"))
                    if not self.hasMoved and self.board.pieces[y-2][x] == 0:
                        self.validMoves.append([x, y-2])
                        self.moveImages.append(self.board.createImage("./move.png", self.validMoves[1], "Move"))
                if x-1 >= 0:
                    if self.board.pieces[y-1][x-1] != 0 and self.board.pieces[y-1][x-1].color == "Black" and self.board.pieces[y-1][x-1].name != "King":
                        self.validKills.append([x-1, y-1])
                        self.killImages.append(self.board.createImage("./kill.png", self.validKills[-1], "Kill"))
                if x+1 <= self.board.rows-1:
                    if self.board.pieces[y-1][x+1] != 0 and self.board.pieces[y-1][x+1].color == "Black" and self.board.pieces[y-1][x+1].name != "King":
                        self.validKills.append([x+1, y-1])
                        self.killImages.append(self.board.createImage("./kill.png", self.validKills[-1], "Kill"))
        else:
            if y+1 <= self.board.cols-1:
                if self.board.pieces[y+1][x] == 0:
                    self.validMoves.append([x, y+1])
                    self.moveImages.append(self.board.createImage("./move.png", self.validMoves[0], "Move"))
                    if not self.hasMoved and self.board.pieces[y+2][x] == 0:
                        self.validMoves.append([x, y+2])
                        self.moveImages.append(self.board.createImage("./move.png", self.validMoves[1], "Move"))
                if x-1 >= 0:
                    if self.board.pieces[y+1][x-1] != 0 and self.board.pieces[y+1][x-1].color == "White" and self.board.pieces[y+1][x-1].name != "King":
                        self.validKills.append([x-1, y+1])
                        self.killImages.append(self.board.createImage("./kill.png", self.validKills[-1], "Kill"))
                if x+1 <= self.board.rows-1:
                    if self.board.pieces[y+1][x+1] != 0 and self.board.pieces[y+1][x+1].color == "White" and self.board.pieces[y+1][x+1].name != "King":
                        self.validKills.append([x+1, y+1])
                        self.killImages.append(self.board.createImage("./kill.png", self.validKills[-1], "Kill"))


    def stopMovement(self, event):
        newX = event.x//self.board.size
        newY = event.y//self.board.size
        enPassantPieces = self.board.enPassantPieces
        self.board.enPassantPieces = []
        if newY == self.board.rows-1 and self.color == "Black":
            Promotion(self.board, self)
        elif newY == 0 and self.color == "White":
            Promotion(self.board, self)
        if newY - self.pos[1] == 2 or self.pos[1] - newY == 2:
            if newX+1 < self.board.rows:
                if self.board.pieces[newY][newX+1] != 0:
                    if self.board.pieces[newY][newX+1].color != self.board.pieces[self.pos[1]][self.pos[0]].color:
                        if self.board.pieces[newY][newX+1].name == "Pawn":
                            self.board.enPassantPieces.append(self.board.pieces[newY][newX+1])
                            self.board.pieces[newY][newX+1].enPassantPositions.append([newX, newY])
                            self.board.pieces[newY][newX+1].validKills.append([newX, newY-1] if self.color == "Black" else [newX, newY+1])
            if newX-1 >= 0:
                if self.board.pieces[newY][newX-1] != 0:
                    if self.board.pieces[newY][newX-1].color != self.board.pieces[self.pos[1]][self.pos[0]].color:
                        if self.board.pieces[newY][newX-1].name == "Pawn":
                            self.board.enPassantPieces.append(self.board.pieces[newY][newX-1])
                            self.board.pieces[newY][newX-1].enPassantPositions.append([newX, newY])
                            self.board.pieces[newY][newX-1].validKills.append([newX, newY-1] if self.color == "Black" else [newX, newY+1])
        if [newX, newY] in self.validMoves:
            self.enPassantPositions = []
            for i in enPassantPieces:
                i.enPassantPositions = []
            self.hasMoved = True
            super().placePiece(newX, newY)
        elif [newX, newY] in self.validKills and not [newX, newY-1] in self.enPassantPositions and not [newX, newY+1] in self.enPassantPositions:
            self.enPassantPositions = []
            for i in enPassantPieces:
                i.enPassantPositions = []
            self.hasMoved = True
            self.Kill(newX, newY, False)
        elif len(self.enPassantPositions) != 0 and [newX, newY] in self.validKills:
            for i in enPassantPieces:
                i.enPassantPositions = []
            if self.color == "White":
                self.Kill(newX, newY+1, [newX, newY])
            else:
                self.Kill(newX, newY-1, [newX, newY])
            self.enPassantPositions = []
            self.hasMoved = True
        else:
            super().returnToOriginalPos()
        for i in self.moveImages:
            self.board.destroyImage(i)
        for i in self.killImages:
            self.board.destroyImage(i)