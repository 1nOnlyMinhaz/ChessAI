from modules.Game import Game
from modules.ValidateKills import ValidateKills
from modules.ValidateMoves import ValidateMoves

class ValidateKing:

    def findChecks(boardArr):
        for row in boardArr:
            for piece in row:
                for pos in ValidateKills.getPossibleKills(piece.pos, piece.piece, piece.colour, piece.moved, boardArr):
                    if boardArr[pos[0]][pos[1]].piece == 1:
                        return [True, boardArr[pos[0]][pos[1]].colour]
        return [False]
    
    def findCheckmate(boardArr, colour):
        for row in boardArr:
            for piece in row:
                if piece.colour == colour:
                    moves = ValidateMoves.getPossibleMoves(piece.pos, piece.piece, piece.colour, piece.moved, boardArr)
                    kills = ValidateKills.getPossibleKills(piece.pos, piece.piece, piece.colour, piece.moved, boardArr)
                    ValidateKing.findCheckedMoves(boardArr, moves, kills, piece)
                    if len(moves) != 0 or len(kills) != 0:
                        return False
        return True

    def findCheckedMoves(BoardArr, moves, kills, self):
        from modules.Pieces import Piece
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
            