import tkinter as tk
from PIL import Image, ImageTk
from modules.Constants import *
from modules.Game import Game

class ValidateMoves:

    def getPossibleMoves(pos, piece,colour, moved, boardArr):
        
        def checkQueen():
            validMoves = []
            for move in checkRook():
                validMoves.append(move)
            for move in checkBishop():
                validMoves.append(move)
            return validMoves

        def checkRook():
            validMoves = []
            pos1 = pos[0]+1
            pos2 = pos[1]+1
            while pos1 < ROWS:
                if boardArr[pos1][pos[1]].piece == 0:
                    validMoves.append([pos1, pos[1]])
                else:
                    break
                pos1 += 1
            while pos2 < COLS:
                if boardArr[pos[0]][pos2].piece == 0:
                    validMoves.append([pos[0], pos2])
                else:
                    break
                pos2 += 1
            pos1 = pos[0]-1
            pos2 = pos[1]-1
            while pos1 >= 0:
                if boardArr[pos1][pos[1]].piece == 0:
                    validMoves.append([pos1, pos[1]])
                else:
                    break
                pos1 -= 1
            while pos2 >= 0:
                if boardArr[pos[0]][pos2].piece == 0:
                    validMoves.append([pos[0], pos2])
                else:
                    break
                pos2 -= 1
            return validMoves
        def checkBishop():
            validMoves = []
            pos1 = pos[0]+1
            pos2 = pos[1]+1
            while pos1 < ROWS and pos2 < COLS:
                if boardArr[pos1][pos2].piece == 0:
                    validMoves.append([pos1, pos2])
                else:
                    break
                pos1 += 1
                pos2 += 1
            pos1 = pos[0]-1
            pos2 = pos[1]-1
            while pos1 >= 0 and pos2 >= 0:
                if boardArr[pos1][pos2].piece == 0:
                    validMoves.append([pos1, pos2])
                else:
                    break
                pos1 -= 1
                pos2 -= 1
            pos1 = pos[0]+1
            pos2 = pos[1]-1
            while pos1 < 8 and pos2 >= 0:
                if boardArr[pos1][pos2].piece == 0:
                    validMoves.append([pos1, pos2])
                else:
                    break
                pos1 += 1
                pos2 -= 1
            pos1 = pos[0]-1
            pos2 = pos[1]+1
            while pos1 >= 0 and pos2 < COLS:
                if boardArr[pos1][pos2].piece == 0:
                    validMoves.append([pos1, pos2])
                else:
                    break
                pos1 -= 1
                pos2 += 1
            return validMoves

        def checkKnight():
            validMoves = []
            possibleMoves = []
            if pos[0]+2 < ROWS:
                if pos[1]+1 < COLS:
                    possibleMoves.append(boardArr[pos[0]+2][pos[1]+1])
                if pos[1]-1 >= 0:
                    possibleMoves.append(boardArr[pos[0]+2][pos[1]-1])
            if pos[0]-2 < COLS and pos[0] > 1:
                if pos[1]+1 < COLS:
                    possibleMoves.append(boardArr[pos[0]-2][pos[1]+1])
                if pos[1]-1 >= 0:
                    possibleMoves.append(boardArr[pos[0]-2][pos[1]-1])
            if pos[1]+2 < COLS:
                if pos[0]+1 < COLS:
                    possibleMoves.append(boardArr[pos[0]+1][pos[1]+2])
                if pos[0]-1 >= 0:
                    possibleMoves.append(boardArr[pos[0]-1][pos[1]+2])
            if pos[1]-2 < COLS and pos[1] > 1:
                if pos[0]+1 < COLS:
                    possibleMoves.append(boardArr[pos[0]+1][pos[1]-2])
                if pos[0]-1 >= 0:
                    possibleMoves.append(boardArr[pos[0]-1][pos[1]-2])
            for piece in possibleMoves:
                if piece.piece == 0 and piece.colour != colour:
                    validMoves.append(piece.pos)
            return validMoves
        
        def checkPawn():
            validMoves = []
            if not moved:
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
                    if pos[0] != ROWS-1:
                        validMoves = []
                        if boardArr[pos[0]+1][pos[1]].piece == 0:
                            validMoves = [[pos[0]+1,pos[1]]]
            return validMoves
        validMoves = []
        if piece == 2: # Pawn move validation.
            validMoves = checkPawn()
        elif piece == 3: # Knight move validation.
            validMoves = checkKnight()
        elif piece == 4: # Bishop move validation
            validMoves = checkBishop()
        elif piece == 5: # Rook move validation
            validMoves = checkRook()
        elif piece == 6: # Queen move validation
            validMoves = checkQueen()
        return validMoves

    def checkEnPassant(colour, pos, boardArr):
        enPassantMoves = []
        if pos[1] != 0 and pos[1] != 7:
            if boardArr[pos[0]][pos[1]+1].piece == 2 and boardArr[pos[0]][pos[1]+1].enPassantValid: # Checks if you can use en passant on the pawn next to it.
                if boardArr[pos[0]][pos[1]-1].piece == 2 and boardArr[pos[0]][pos[1]-1].enPassantValid: # Changing this so the en passant moves are in a list. Gotta make the changes to FindKills() too.
                    enPassantMoves.append(pos[1]-1)
                enPassantMoves.append(pos[1]+1)
            elif boardArr[pos[0]][pos[1]-1].piece == 2 and boardArr[pos[0]][pos[1]-1].enPassantValid:
                enPassantMoves.append(pos[1]-1)
            return [True, enPassantMoves]
        elif pos[1] == 0:
            if boardArr[pos[0]][pos[1]+1].piece == 2 and boardArr[pos[0]][pos[1]+1].enPassantValid: # Checks if you can use en passant on the pawn next to it.
                enPassantMoves.append(pos[1]+1)
                return [True, enPassantMoves]
        else:
            if boardArr[pos[0]][pos[1]-1].piece == 2 and boardArr[pos[0]][pos[1]-1].enPassantValid: # Checks if you can use en passant on the pawn next to it.
                enPassantMoves.append(pos[1]-1)
                return [True, enPassantMoves]
        return [False, 404]
    
    def checkEnPassantValid(colour, pos, boardArr, moved):
        if colour == "Black":
            condition1 = False
            condition2 = False
            if pos[1] != 7:
                condition1 = boardArr[pos[0]][pos[1]+1].piece == 2 and boardArr[pos[0]][pos[1]+1].colour == "White"
            if pos[1] != 0:
                condition2 = boardArr[pos[0]][pos[1]-1].piece == 2 and boardArr[pos[0]][pos[1]-1].colour == "White"
            if pos[1] != 0 and pos[1] != 7:
                if condition1 or condition2:
                    if pos[0] == 3 and not moved:
                        return True
            elif pos[1] == 0:
                if condition1:
                    if pos[0] == 3 and not moved:
                        return True
            else:
                if condition2:
                    if pos[0] == 3 and not moved:
                        return True
        else:
            if colour == "Black":
                condition1 = False
                condition2 = False
            if pos[1] != 7:
                condition1 = boardArr[pos[0]][pos[1]+1].piece == 2 and boardArr[pos[0]][pos[1]+1].colour == "Black"
            if pos[1] != 0:
                condition2 = boardArr[pos[0]][pos[1]-1].piece == 2 and boardArr[pos[0]][pos[1]-1].colour == "Black"
            if pos[1] != 0 and pos[1] != 7:
                #print(boardArr[pos[0]][pos[1]+1])
                if condition1 or condition2:
                    if pos[0] == 4 and not moved:
                        return True
            elif pos[1] == 0:
                if condition1:
                    if pos[0] == 4 and not moved:
                        return True
            else:
                if condition2 and not moved:
                    if pos[0] == 4:
                        return True
        return False

class ValidateKills:
    def getPossibleKills(pos, piece, colour, moved, boardArr):
            validKills = []
            from modules.Pieces import Piece
            def checkQueen():
                validKills = []
                for kill in checkRook():
                    validKills.append(kill)
                for kill in checkBishop():
                    validKills.append(kill)
                return validKills
            def checkRook():
                validKills = []
                pos1 = pos[0]+1
                pos2 = pos[1]+1
                while pos1 < 8:
                    if boardArr[pos1][pos[1]].piece != 0 and boardArr[pos1][pos[1]].colour != colour:
                        validKills.append([pos1, pos[1]])
                        break
                    elif boardArr[pos1][pos[1]].piece != 0:
                        break
                    pos1 += 1
                while pos2 < 8:
                    if boardArr[pos[0]][pos2].piece != 0 and boardArr[pos[0]][pos2].colour != colour:
                        validKills.append([pos[0], pos2])
                        break
                    elif boardArr[pos[0]][pos2].piece != 0:
                        break
                    pos2 += 1
                pos1 = pos[0]-1
                pos2 = pos[1]-1
                while pos1 >= 0:
                    if boardArr[pos1][pos[1]].piece != 0 and boardArr[pos1][pos[1]].colour != colour:
                        validKills.append([pos1, pos[1]])
                        break
                    elif boardArr[pos1][pos[1]].piece != 0:
                        break
                    pos1 -= 1
                while pos2 >= 0:
                    if boardArr[pos[0]][pos2].piece != 0 and boardArr[pos[0]][pos2].colour != colour:
                        validKills.append([pos[0], pos2])
                        break
                    elif boardArr[pos[0]][pos2].piece != 0:
                        break
                    pos2 -= 1
                return validKills

            def checkBishop():
                validKills = []
                pos1 = pos[0]+1
                pos2 = pos[1]+1
                while pos1 < 8 and pos2 < 8:
                    if boardArr[pos1][pos2].piece != 0 and boardArr[pos1][pos2].colour != colour:
                        validKills.append([pos1, pos2])
                        break
                    elif boardArr[pos1][pos2].piece != 0:
                        break
                    pos1 += 1
                    pos2 += 1
                pos1 = pos[0]-1
                pos2 = pos[1]-1
                while pos1 >= 0 and pos2 >= 0:
                    if boardArr[pos1][pos2].piece != 0 and boardArr[pos1][pos2].colour != colour:
                        validKills.append([pos1, pos2])
                        break
                    elif boardArr[pos1][pos2].piece != 0:
                        break
                    pos1 -= 1
                    pos2 -= 1
                pos1 = pos[0]+1
                pos2 = pos[1]-1
                while pos1 < 8 and pos2 >= 0:
                    if boardArr[pos1][pos2].piece != 0 and boardArr[pos1][pos2].colour != colour:
                        validKills.append([pos1, pos2])
                        break
                    elif boardArr[pos1][pos2].piece != 0:
                        break
                    pos1 += 1
                    pos2 -= 1
                pos1 = pos[0]-1
                pos2 = pos[1]+1
                while pos1 >= 0 and pos2 < 8:
                    if boardArr[pos1][pos2].piece != 0 and boardArr[pos1][pos2].colour != colour:
                        validKills.append([pos1, pos2])
                        break
                    elif boardArr[pos1][pos2].piece != 0:
                        break
                    pos1 -= 1
                    pos2 += 1
                return validKills

            def checkKnight():
                validKills = []
                possibleKills = []
                if pos[0]+2 < 8:
                    if pos[1]+1 < 8:
                        possibleKills.append(boardArr[pos[0]+2][pos[1]+1])
                    if pos[1]-1 >= 0:
                        possibleKills.append(boardArr[pos[0]+2][pos[1]-1])
                if pos[0]-2 < 8 and pos[0] > 1:
                    if pos[1]+1 < 8:
                        possibleKills.append(boardArr[pos[0]-2][pos[1]+1])
                    if pos[1]-1 >= 0:
                        possibleKills.append(boardArr[pos[0]-2][pos[1]-1])
                if pos[1]+2 < 8:
                    if pos[0]+1 < 8:
                        possibleKills.append(boardArr[pos[0]+1][pos[1]+2])
                    if pos[0]-1 >= 0:
                        possibleKills.append(boardArr[pos[0]-1][pos[1]+2])
                if pos[1]-2 < 8 and pos[1] > 1:
                    if pos[0]+1 < 8:
                        possibleKills.append(boardArr[pos[0]+1][pos[1]-2])
                    if pos[0]-1 >= 0:
                        possibleKills.append(boardArr[pos[0]-1][pos[1]-2])
                for piece in possibleKills:
                    if piece.piece != 0 and piece.colour != colour:
                        validKills.append(piece.pos)
                return validKills

            def checkPawn():
                validKills = []
                EnPassantInfo = ValidateMoves.checkEnPassant(colour, pos, boardArr)
                if EnPassantInfo[0]:
                    for position in EnPassantInfo[1]:
                        if colour == "White":
                            validKills.append([pos[0]-1, position])
                        else:
                            validKills.append([pos[0]+1, position])
                if colour == "White":
                    if pos[1] != 0:
                        if boardArr[pos[0]-1][pos[1]-1].piece != 0 and boardArr[pos[0]-1][pos[1]-1].colour != boardArr[pos[0]][pos[1]].colour:
                            validKills.append([pos[0]-1, pos[1]-1])
                    if pos[1] != 7:
                        if boardArr[pos[0]-1][pos[1]+1].piece != 0 and boardArr[pos[0]-1][pos[1]+1].colour != boardArr[pos[0]][pos[1]].colour:
                            validKills.append([pos[0]-1, pos[1]+1])
                else:
                    if pos[1] != 0:
                        if boardArr[pos[0]+1][pos[1]-1].piece != 0 and boardArr[pos[0]+1][pos[1]-1].colour != boardArr[pos[0]][pos[1]].colour:
                            validKills.append([pos[0]+1,pos[1]-1])
                    if pos[1] != 7:
                        if boardArr[pos[0]+1][pos[1]+1].piece != 0 and boardArr[pos[0]+1][pos[1]+1].colour != boardArr[pos[0]][pos[1]].colour:
                            validKills.append([pos[0]+1,pos[1]+1])
                return validKills

            if piece == Piece.Pawn: # Pawn kill validation
                validKills = checkPawn()
            elif piece == Piece.Knight:
                validKills = checkKnight()
            elif piece == Piece.Bishop:
                validKills = checkBishop()
            elif piece == Piece.Rook:
                validKills = checkRook()
            elif piece == Piece.Queen:
                validKills = checkQueen()
            return validKills

class ValidateKing:

    def findChecks(boardArr):
        for row in boardArr:
            for piece in row:
                for pos in ValidateKills.getPossibleKills(piece.pos, piece.piece, piece.colour, piece.moved, boardArr):
                    if boardArr[pos[0]][pos[1]].piece == 1:
                        print("Check!")
                        return [True, boardArr[pos[0]][pos[1]].colour]
        return [False]
    
    def findCheckedMoves(BoardArr, moves, kills, self):
        from modules.Pieces import Piece
        if not Game.WhiteKingChecked and not Game.BlackKingChecked:
            checkedMoves = []
            for pos in moves:
                BoardArr[pos[0]][pos[1]] = BoardArr[self.pos[0]][self.pos[1]]
                BoardArr[self.pos[0]][self.pos[1]] = Piece(self.board, 0, self.pos, "None")
                if ValidateKing.findChecks(BoardArr)[0]:
                    checkedMoves.append(pos)
                BoardArr[self.pos[0]][self.pos[1]] = BoardArr[pos[0]][pos[1]]
                BoardArr[pos[0]][pos[1]] = Piece(self.board, 0, pos, "None")
            for pos in checkedMoves:
                moves.remove(pos)
            checkedKills = []
            for pos in kills:
                temp1 = BoardArr[pos[0]][pos[1]]
                BoardArr[pos[0]][pos[1]] = BoardArr[self.pos[0]][self.pos[1]]
                BoardArr[self.pos[0]][self.pos[1]] = Piece(self.board, 0, self.pos, "None")
                if ValidateKing.findChecks(BoardArr)[0]:
                    checkedKills.append(pos)
                BoardArr[self.pos[0]][self.pos[1]] = BoardArr[pos[0]][pos[1]]
                BoardArr[pos[0]][pos[1]] = temp1
            for pos in checkedKills:
                kills.remove(pos)