import tkinter as tk
from PIL import Image, ImageTk
from modules.Board import Board
from modules.Pieces import Piece as Pieces
from modules.Constants import *
window = tk.Tk()

window.title("ChessAI")
window.iconbitmap("icon.ico")
window.configure(bg="#F6D686")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(False, False)

board = Board(window,WIDTH,HEIGHT)

board.LoadPiecesFromFen(board.canvas, "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr w KQkq - 0 1") #Loads starting board.

window.mainloop()

