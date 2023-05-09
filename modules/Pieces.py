import tkinter as tk
from PIL import Image, ImageTk
from modules.ValidateMoves import ValidateMoves
from modules.Constants import *
import modules.Movement as Movement

class Piece:
    imagesBlack = {}
    imagesWhite = {}
    King = 1
    Pawn = 2
    Knight = 3
    Bishop = 4
    Rook = 5
    Queen = 6
    White = 8
    Black = 16
    pieceList = ["k","p","n","b","r","q"]
    rectIDs = []
    def __init__(self, board, piece, pos, colour):
        self.board = board
        self.piece = int(piece)
        self.pos = pos
        self.colour = colour
        self.moved = False
        self.imageIDs = []
        self.firstMove = True # To be removed
        self.validMoves = []
        self.validKills = []
        if self.piece == Piece.Pawn:
            self.enPassantValid = False # Make sure the EnPassant checking is up to date
        # If the image has not been loaded yet, load it and add it to the dictionary
        if self.piece != 0:
            if colour == "Black":
                if piece not in Piece.imagesBlack:
                    img = Image.open("Pieces/"+colour+"/"+piece+".png")
                    img = img.convert("RGBA")
                    Piece.imagesBlack[piece] = img

                # Get the Image object from the dictionary and create the canvas image button
                img = Piece.imagesBlack[piece]
                self.photo_image = ImageTk.PhotoImage(img)
                self.button_id = board.create_image(SQSIZE*pos[1], SQSIZE*pos[0], image=self.photo_image, anchor="nw")
                board.tag_bind(self.button_id, "<B1-Motion>", self.movePiece)
                board.tag_bind(self.button_id, "<ButtonPress>", self.startMovement)
                board.tag_bind(self.button_id, "<ButtonRelease>", self.stopMovement)

            else:
                if piece not in Piece.imagesWhite:
                    img = Image.open("Pieces/"+colour+"/"+piece+".png")
                    img = img.convert("RGBA")
                    Piece.imagesWhite[piece] = img

                # Get the Image object from the dictionary and create the canvas image button
                img = Piece.imagesWhite[piece]
                self.photo_image = ImageTk.PhotoImage(img)
                self.button_id = board.create_image(SQSIZE*pos[1], SQSIZE*pos[0], image=self.photo_image, anchor="nw")
                board.tag_bind(self.button_id, "<B1 - Motion>", self.movePiece)
                board.tag_bind(self.button_id, "<ButtonPress>", self.startMovement)
                board.tag_bind(self.button_id, "<ButtonRelease>", self.stopMovement)

    def movePiece(self, event):
        Movement.movePiece(self, event)
    
    def startMovement(self, event):
        Movement.startMovement(self, event)

    def stopMovement(self, event):
        Movement.stopMovement(self, event)