from modules.Constants import *

class ValidateMoves:

    def getPossibleMoves(pos, piece,colour, moved, boardArr):

        def checkKing():
            validMoves = []
            if pos[0]+1 < ROWS and boardArr[pos[0]+1][pos[1]].piece == 0:
                validMoves.append([pos[0]+1, pos[1]])
            if pos[1]+1 < COLS and boardArr[pos[0]][pos[1]+1].piece == 0:
                validMoves.append([pos[0],pos[1]+1])
            if pos[0]-1 >= 0 and boardArr[pos[0]-1][pos[1]].piece == 0:
                validMoves.append([pos[0]-1, pos[1]])
            if pos[1]-1 >= 0 and boardArr[pos[0]][pos[1]-1].piece == 0:
                validMoves.append([pos[0], pos[1]-1])
            if pos[0]+1 < ROWS and pos[1]+1 < COLS and boardArr[pos[0]+1][pos[1]+1].piece == 0:
                validMoves.append([pos[0]+1, pos[1]+1])
            if pos[0]+1 < ROWS and pos[1]-1 >= 0 and boardArr[pos[0]+1][pos[1]-1].piece == 0:
                validMoves.append([pos[0]+1, pos[1]-1])
            if pos[0]-1 >= 0 and pos[1]+1 < COLS and boardArr[pos[0]-1][pos[1]+1].piece == 0:
                validMoves.append([pos[0]-1, pos[1]+1])
            if pos[0]-1 >= 0 and pos[1]-1 >= 0 and boardArr[pos[0]-1][pos[1]-1].piece == 0:
                validMoves.append([pos[0]-1, pos[1]-1])
            return validMoves
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

        if piece == 1: # King move validation
            validMoves = checkKing( )
        elif piece == 2: # Pawn move validation.
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
