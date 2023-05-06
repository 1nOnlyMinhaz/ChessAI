import tkinter as tk
from PIL import Image, ImageTk


class ValidateMoves:
    def getPossibleMoves(pos, piece,colour, moved, boardArr):
        validMoves = []   
        if piece == 2: # Pawn move validation.
            if not moved:
                print(pos)
                print(colour)
                if colour == "White":
                    if boardArr[pos[0]-1][pos[1]].piece == 0:
                        validMoves = [[pos[0]-1,pos[1]]]
                        if boardArr[pos[0]-2][pos[1]].piece == 0:
                            validMoves = [[pos[0]-1,pos[1]],[pos[0]-2,pos[1]]]
                else: # If the colour is black
                    if boardArr[pos[0]+1][pos[1]].piece == 0:
                        validMoves = [[pos[0]+1,pos[1]]]
                        if boardArr[pos[0]+2][pos[1]].piece == 0:
                            validMoves = [[pos[0]+1,pos[1]],[pos[0]+2,pos[1]]]
            else:
                if colour == "White":
                    if pos[0] != 0:
                        validMoves = []
                        if boardArr[pos[0]-1][pos[1]].piece == 0:
                            validMoves = [[pos[0]-1,pos[1]]]
                else: # If the colour is black
                    if pos[0] != 7:
                        validMoves = []
                        if boardArr[pos[0]+1][pos[1]].piece == 0:
                            validMoves = [[pos[0]+1,pos[1]]]
        return validMoves

    def checkEnPassant(colour, pos, boardArr):
        enPassantMoves = []
        if pos[1] != 0 and pos[1] != 7:
            if boardArr[pos[0]][pos[1]+1].piece == 2 and boardArr[pos[0]][pos[1]+1].enPassantValid: # Checks if you can use en passant on the pawn next to it.
                if boardArr[pos[0]][pos[1]-1].piece == 2 and boardArr[pos[0]][pos[1]-1].enPassantValid: # Changing this so the en passant moves are in a list. Gotta make the changes to FindKills() too.
                    enPassantMoves.append(pos[0]+1)
                enPassantMoves.append(pos[0]-1)
                return [True, enPassantMoves]
        elif pos[1] == 0:
            if boardArr[pos[0]][pos[1]+1].piece == 2 and boardArr[pos[0]][pos[1]+1].enPassantValid: # Checks if you can use en passant on the pawn next to it.
                enPassantMoves.append(pos[0]-1)
                return [True, enPassantMoves]
        else:
            if boardArr[pos[0]][pos[1]-1].piece == 2 and boardArr[pos[0]][pos[1]-1].enPassantValid: # Checks if you can use en passant on the pawn next to it.
                enPassantMoves.append(pos[0]+1)
                return [True, enPassantMoves]
        return [False, 404]
    
    def checkEnPassantValid(colour, pos, boardArr):
        if colour == "Black":
            condition1 = boardArr[pos[0]][pos[1]+1].piece == 2 and boardArr[pos[0]][pos[1]+1].colour == "White"
            condition2 = boardArr[pos[0]][pos[1]-1].piece == 2 and boardArr[pos[0]][pos[1]-1].colour == "White"
            if pos[1] != 0 and pos[1] != 7:
                if condition1 or condition2:
                    if pos[0] == 3:
                        print("En passant!")
                        return True
            elif pos[1] == 0:
                if condition1:
                    if pos[0] == 3:
                        print("En passant!")
                        return True
            else:
                if condition2:
                    if pos[0] == 3:
                        print("En passant!")
                        return True
        else:
            condition1 = boardArr[pos[0]][pos[1]+1].piece == 2 and boardArr[pos[0]][pos[1]+1].colour == "Black"
            condition2 = boardArr[pos[0]][pos[1]-1].piece == 2 and boardArr[pos[0]][pos[1]-1].colour == "Black"
            if pos[1] != 0 and pos[1] != 7:
                #print(boardArr[pos[0]][pos[1]+1])
                if condition1 or condition2:
                    if pos[0] == 4:
                        print("En passant!")
                        return True
            elif pos[1] == 0:
                if condition1:
                    if pos[0] == 4:
                        print("En passant!")
                        return True
            else:
                if condition2:
                    if pos[0] == 4:
                        print("En passant!")
                        return True
        return False

class ValidateKills:
    def getPossibleKills(pos, piece, colour, moved, boardArr):
            if piece == 2:
                validKills = []
                EnPassantInfo = ValidateMoves.checkEnPassant(colour, pos, boardArr)
                print(EnPassantInfo)
                if EnPassantInfo[0]:
                    for position in EnPassantInfo[1]:
                        if colour == "White":
                            validKills.append([position, pos[1]+1])
                        else:
                            validKills.append([position, pos[1]-1])
                if colour == "White":
                    if boardArr[pos[0]-1][pos[1]-1].piece != 0:
                        validKills.append([pos[0]-1, pos[1]-1])
                    if boardArr[pos[0]-1][pos[1]+1].piece != 0:
                        validKills.append([pos[0]-1, pos[1]+1])
                else:
                    if boardArr[pos[0]+1][pos[1]-1].piece != 0:
                        validKills.append([pos[0]+1,pos[1]-1])
                    if boardArr[pos[0]+1][pos[1]+1].piece != 0:
                        validKills.append([pos[0]+1,pos[1]+1])
                return validKills