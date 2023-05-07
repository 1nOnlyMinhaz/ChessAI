from modules.Board import Board
from modules.Pieces import Piece
def Kill(board, pos, colour):
    if Board.boardArr[pos[0]][pos[1]].piece == 0:
        if colour == "White" and Board.boardArr[pos[0]+1][pos[1]].piece == Piece.Pawn:
            id = Board.boardArr[pos[0]+1][pos[1]].button_id
            pos = [pos[0]+1, pos[1]]
        elif colour == "Black" and Board.boardArr[pos[0]-1][pos[1]].piece == Piece.Pawn:
            id = Board.boardArr[pos[0]-1][pos[1]].button_id
            pos = [pos[0]-1, pos[1]]
    else:
        id = Board.boardArr[pos[0]][pos[1]].button_id
    board.delete(id)
    Board.boardArr[pos[0]][pos[1]] = Piece(board, 0, pos, "None")

