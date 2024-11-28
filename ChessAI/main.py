import tkinter
import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk
import modules.Constants as Constants
from modules.Board import Board
from math import sin, cos, pi
from typing import Iterator


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('ChessAI')
        self.geometry(f'{Constants.WIDTH}x{Constants.HEIGHT}')
        self.iconbitmap("icon.ico")
        self.minsize(Constants.WIDTH, Constants.HEIGHT)
        self.configure(background="#333333")
        self.promotionUI = False
        canvas = tkinter.Canvas(self, bg="#333333", bd="0", highlightthickness="0")
        canvas.pack()

        self.canvas = canvas
        self.bind("<Configure>", self.onResize)
        self.board = Board(self.canvas, Constants.ROWS, Constants.COLS, self)

    def onResize(self, event):
        size = min(event.width, event.height)
        if self.canvas.winfo_width() == size or self.canvas.winfo_height() == size:
            print("No resize")
            return
        self.canvas.config(width=size, height=size)
        if self.promotionUI:
            pass
        self.board.Resize(size//Constants.ROWS)


Window().mainloop()