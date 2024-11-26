
class Piece:
    def __init__(self, board, name, color, position):
        self.board = board
        self.color = color
        self.name = name
        self.pos = position
        self.validMoves = []
        self.validKills = []
        self.moveImages = []
        self.killImages = []
        board.pieces[self.pos[1]][self.pos[0]] = self
        self.image = board.createImage(f"./Pieces/{color}/{name}.png", position, "Piece")
        self.board.canvas.tag_bind(self.image, "<B1-Motion>", self.movePiece)
        self.board.canvas.tag_bind(self.image, "<ButtonPress>", self.startMovement)
        self.board.canvas.tag_bind(self.image, "<ButtonRelease>", self.stopMovement)

    def movePiece(self, event):
        MAXPIECEX = self.board.canvas.winfo_reqwidth()-self.board.size
        MAXPIECEY = self.board.canvas.winfo_reqheight()-self.board.size
        # Get the current position of the mouse
        x = event.x - (self.board.size / 2) if event.x > (self.board.size / 2) else 0
        y = event.y - (self.board.size / 2) if event.y > (self.board.size / 2) else 0
        x = MAXPIECEX if x > MAXPIECEX else x
        y = MAXPIECEY if x > MAXPIECEY else y
        # Move the image to the new position
        self.board.canvas.coords(self.image, x, y)
        self.board.canvas.lift(self.image)

    def startMovement(self, event):
        print("Caution: this piece does not check any movement")

    def stopMovement(self, event):
        newX = event.x // self.board.size
        newY = event.y // self.board.size
        if self.board.pieces[newY][newX] != 0 or self.board.CurrentColour != self.color:
            self.returnToOriginalPos()
            return
        self.placePiece(newX, newY)

    def Kill(self, newX, newY, enPassant):
        self.validKills = []
        self.board.destroyImage(self.board.pieces[newY][newX].image)
        if enPassant:
            self.placePiece(enPassant[0], enPassant[1])
            self.board.pieces[newY][newX] = 0
        else:
            self.placePiece(newX, newY)

    def placePiece(self, newX, newY):
        self.validMoves = []
        self.board.CurrentColour = "White" if self.board.CurrentColour == "Black" else "Black"
        self.board.pieces[self.pos[1]][self.pos[0]] = 0
        self.pos[0] = newX
        self.pos[1] = newY
        if self.pos[0] > self.board.rows-1:
            self.pos[0] = self.board.rows-1
        if self.pos[1] > self.board.cols-1:
            self.pos[1] = self.board.cols-1
        if self.pos[0] < 0:
            self.pos[0] = 0
        if self.pos[1] < 0:
            self.pos[1] = 0
        self.board.pieces[self.pos[1]][self.pos[0]] = self
        self.board.canvas.coords(self.image, self.pos[0]*self.board.size, self.pos[1]*self.board.size)
        return self

    def returnToOriginalPos(self):
        self.validMoves = []
        self.board.canvas.coords(self.image, self.pos[0] * self.board.size, self.pos[1] * self.board.size)



class Rook(Piece):
    def __init__(self, board, color, position):
        super().__init__(board, "Rook", color, position)
        self.board = board
        self.color = color
        self.pos = position

class Bishop(Piece):
    def __init__(self, board, color, position):
        super().__init__(board, "Bishop", color, position)
        self.board = board
        self.color = color
        self.pos = position

class Knight(Piece):
    def __init__(self, board, color, position):
        super().__init__(board, "Knight", color, position)
        self.board = board
        self.color = color
        self.pos = position

class Queen(Piece):
    def __init__(self, board, color, position):
        super().__init__(board, "Queen", color, position)
        self.board = board
        self.color = color
        self.pos = position

class King(Piece):
    def __init__(self, board, color, position):
        super().__init__(board, "King", color, position)
        self.board = board
        self.color = color
        self.pos = position


