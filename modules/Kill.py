from modules.Board import Board
from modules.Pieces import Piece
def Kill(board, id, pos, colour):
    board.delete(id)
    Board.boardArr[pos[0]][pos[1]] = Piece(board, 0, pos, colour)


