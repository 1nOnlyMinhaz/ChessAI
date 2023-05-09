from modules.ValidateMoves import ValidateMoves
from modules.Constants import *

class ValidateKills:
    def getPossibleKills(pos, piece, colour, moved, boardArr):
            validKills = []
            from modules.Pieces import Piece

            def checkKing():
                validKills = []
                if pos[0]+1 < ROWS and boardArr[pos[0]+1][pos[1]].piece != 0 and boardArr[pos[0]+1][pos[1]].colour != colour:
                    validKills.append([pos[0]+1, pos[1]])
                if pos[1]+1 < COLS and boardArr[pos[0]][pos[1]+1].piece != 0 and boardArr[pos[0]][pos[1]+1].colour != colour:
                    validKills.append([pos[0],pos[1]+1])
                if pos[0]-1 >= 0 and boardArr[pos[0]-1][pos[1]].piece != 0 and boardArr[pos[0]-1][pos[1]].colour != colour:
                    validKills.append([pos[0]-1, pos[1]])
                if pos[1]-1 >= 0 and boardArr[pos[0]][pos[1]-1].piece != 0 and boardArr[pos[0]][pos[1]-1].colour != colour:
                    validKills.append([pos[0], pos[1]-1])
                if pos[0]+1 < ROWS and pos[1]+1 < COLS and boardArr[pos[0]+1][pos[1]+1].piece != 0 and boardArr[pos[0]+1][pos[1]+1].colour != colour:
                    validKills.append([pos[0]+1, pos[1]+1])
                if pos[0]+1 < ROWS and pos[1]-1 >= 0 and boardArr[pos[0]+1][pos[1]-1].piece != 0 and boardArr[pos[0]+1][pos[1]-1].colour != colour:
                    validKills.append([pos[0]+1, pos[1]-1])
                if pos[0]-1 >= 0 and pos[1]+1 < COLS and boardArr[pos[0]-1][pos[1]+1].piece != 0 and boardArr[pos[0]-1][pos[1]+1].colour != colour:
                    validKills.append([pos[0]-1, pos[1]+1])
                if pos[0]-1 >= 0 and pos[1]-1 >= 0 and boardArr[pos[0]-1][pos[1]-1].piece != 0 and boardArr[pos[0]-1][pos[1]-1].colour != colour:
                    validKills.append([pos[0]-1, pos[1]-1])
                return validKills

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

            if piece == Piece.King:
                validKills = checkKing()
            elif piece == Piece.Pawn: # Pawn kill validation
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