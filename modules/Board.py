import tkinter as tk
from PIL import Image, ImageTk
from modules.Pieces import Piece
from modules.Constants import *

class Board:
    boardArr = []
    def __init__(self, window, width, height):
        # Create a canvas widget to draw on
        self.window = window
        self.width = width
        self.height = height
        Board.boardArr = [[0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0]]
        img = Image.open("move.png")
        self.photoImage1 = ImageTk.PhotoImage(img)
        print(self.photoImage1, "    THE DOT")
        img2 = Image.open("kill.png").convert("RGBA")
        self.photoImage2 = ImageTk.PhotoImage(img2)
        canvas = tk.Canvas(window, width=width, height=height)
        canvas.pack()
        self.canvas = canvas
        for i in range(ROWS):
            for j in range(COLS):
                Board.boardArr[i][j] = Piece(canvas, 0, [i, j], "None")
        # Draw the squares of the chess board
        for row in range(8):
            for col in range(8):
                x1 = col * SQSIZE
                y1 = row * SQSIZE
                x2 = x1 + SQSIZE
                y2 = y1 + SQSIZE
                if (row + col) % 2 == 0:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="#C74C51", outline = "#F6D686")
                else:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="#303030", outline = "#F6D686")

    def LoadPiecesFromFen(self, board, fen):
        boardArr = Board.boardArr
        pieceTypeFromSymbol = {
            "k": Piece.King,
            "p": Piece.Pawn,
            "n": Piece.Knight,
            "b": Piece.Bishop,
            "r": Piece.Rook,
            "q": Piece.Queen
        }
        col = 0
        row = ROWS - 1

        # Don't wanna actually make any changes to the algorithm, just the adding to the array part.

        fenBoard = fen.split(" ")[0]

        for symbol in fenBoard:
            if symbol == "/":
                col = 0
                row -= 1
            elif symbol.isnumeric():
                col += int(symbol)
            elif symbol.isupper():
                newPiece = Piece(board, str(pieceTypeFromSymbol[symbol.lower()]),[row,col],"White") # Starting work here, all the instances are gonna replace the symbols in boardArr
                boardArr[row][col] = newPiece # was originally the symbol
                col+=1
            elif symbol.islower():
                newPiece = Piece(board, str(pieceTypeFromSymbol[symbol]), [row, col], "Black")
                boardArr[row][col] = newPiece # same here
                col+=1
        print(boardArr)

    def showMove(pos, board):
        x1 = pos[1] * SQSIZE
        y1 = pos[0] * SQSIZE
        x2 = x1+SQSIZE
        y2 = y1+SQSIZE
        # board.create_rectangle(x1, y1, x2, y2, fill=colour, width = 0)
        id = board.create_image(x1, y1, image="pyimage1", anchor="nw")
        return id
    
    def showKill(pos, board):
        x1 = pos[1] * SQSIZE
        y1 = pos[0] * SQSIZE
        x2 = x1+SQSIZE
        y2 = y1+SQSIZE
       # board.create_rectangle(x1, y1, x2, y2, fill=colour, width = 0)
        id = board.create_image(x1, y1, image="pyimage2", anchor="nw")
        return id
