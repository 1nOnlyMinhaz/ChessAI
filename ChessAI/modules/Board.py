import modules.Constants as Constants
from modules.Constants import SQSIZE
from modules.Pieces import *
from modules.Pawn import Pawn
from PIL import Image, ImageTk
import tkinter as tk

class Board:
    def __init__(self, canvas, rows, cols, window):
        self.canvas = canvas
        self.rows = rows
        self.cols = cols
        self.size = SQSIZE
        self.squares = []
        self.pieces = [[0 for i in range(self.cols)] for i in range(self.rows)]
        self.enPassantPieces = []
        self.photoImages = []
        self.originalImages = []
        self.images = {}
        self.imageObjects = []
        self.resizeDebounce = False
        self.window = window

        self.CurrentColour = "White"
        y1 = 0
        for row in range(self.rows):
            x1 = 0
            x2 = Constants.SQSIZE
            y2 = y1 + Constants.SQSIZE
            for col in range(self.cols):
                x2 = x1 + Constants.SQSIZE
                if (row + col) % 2 == 0:
                    self.squares.append(canvas.create_rectangle(x1, y1, x2, y2, fill="#C74C51", outline="#F6D686"))
                else:
                    self.squares.append(canvas.create_rectangle(x1, y1, x2, y2, fill="#303030", outline="#F6D686"))
                x1 = x2
            y1 = y2


        # Load all pieces
        for i in range(8):
            Pawn(self, "Black", [i, 1])
        for i in range(8):
            Pawn(self, "White", [i, 6])
        Rook(self, "Black", [0, 0])
        Rook(self, "Black", [7, 0])
        Knight(self, "Black", [1, 0])
        Bishop(self, "Black", [2, 0])
        Queen(self, "Black", [3, 0])
        King(self, "Black", [4, 0])
        Bishop(self, "Black", [5, 0])
        Knight(self, "Black", [6, 0])
        Rook(self, "White", [0, 7])
        Rook(self, "White", [7, 7])
        Knight(self, "White", [1, 7])
        Bishop(self, "White", [2, 7])
        Queen(self, "White", [3, 7])
        King(self, "White", [4, 7])
        Bishop(self, "White", [5, 7])
        Knight(self, "White", [6, 7])


    def Resize(self, newSize):
        size_ratio = newSize / self.size
        y1 = 0
        for row in range(self.rows):
            x1 = 0
            x2 = newSize
            y2 = y1 + newSize
            for col in range(self.cols):
                x2 = x1 + newSize
                self.canvas.coords(self.squares[(row*self.rows)+col], x1, y1, x2, y2)
                x1 = x2
            y1 = y2

        for i in range(len(self.originalImages)):
            if str(newSize)+str(self.imageObjects[i]) in self.images.keys():
                image = self.images[str(newSize)+str(self.imageObjects[i])]
            else:
                image = self.originalImages[i]
                image = image.resize((newSize, newSize), Image.Resampling.BILINEAR)
                if len(self.images.keys()) < 500:
                    self.images[str(newSize)+str(self.imageObjects[i])] = image
                elif len(self.images.keys()) == 499:
                    print("Limit reached")
            self.photoImages[i] = ImageTk.PhotoImage(image)
            self.canvas.itemconfig(self.imageObjects[i], image=self.photoImages[i])
            x, y = self.canvas.coords(self.imageObjects[i])
            self.canvas.coords(self.imageObjects[i], x*size_ratio, y*size_ratio)
        self.size = newSize


    def createImage(self, fileName: str, position, type):
        """
        :param type:
        :param fileName: The name of the image file
        :param position: The position of the image on the board
        :return: 
        """
        img = Image.open(fileName)
        img = img.convert("RGBA")
        maxSize = self.window.winfo_screenheight() // Constants.COLS
        img = img.resize((maxSize, maxSize), Image.Resampling.LANCZOS)
        if type == "Piece":
            self.originalImages.append(img)
            img = img.resize((self.size, self.size), Image.Resampling.LANCZOS)
            self.photoImages.append(ImageTk.PhotoImage(img))
            imageObject = self.canvas.create_image(position[0]*self.size, position[1]*self.size, image=self.photoImages[-1], anchor="nw")
            self.imageObjects.append(imageObject)
        else:
            img = img.resize((self.size, self.size), Image.Resampling.LANCZOS)
            self.photoImages.append(ImageTk.PhotoImage(img))
            imageObject = self.canvas.create_image(position[0]*self.size, position[1]*self.size, image=self.photoImages[-1], anchor="nw")
        return imageObject

    def destroyImage(self, imageObject):
        if imageObject in self.imageObjects:
            self.originalImages.pop(self.imageObjects.index(imageObject))
            self.imageObjects.remove(imageObject)
            for key in [i for i in self.images if str(imageObject) in i]:
                del self.images[key]
        self.canvas.delete(imageObject)
