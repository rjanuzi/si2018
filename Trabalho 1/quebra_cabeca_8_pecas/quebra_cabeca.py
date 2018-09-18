import random
from enum import Enum

class Dir(Enum):
    L = 1
    R = 2
    U = 3
    D = 4

class Puzzle:
    def __init__(self):
        pieces = list(range(9))
        random.shuffle(pieces)
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        k = 0
        for i in range(3):
            for j in range(3):
                self.board[i][j] = pieces[k]
                k += 1

    def isDone(self):
        k = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != k:
                    return False
                else:
                    k += 1
        return True

    def findPiece(self, piece=0):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == piece:
                    return i,j

    def equals(self, other):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != other.board[i][j]:
                    return False
        return True

    def copy(self):
        new = Puzzle()
        for i in range(3):
            for j in range(3):
                new.board[i][j] = self.board[i][j]
        return new

    def move(self, dir):
        """Move to a direction (Dir Enum)"""
        freePosition = self.findPiece()

        # Free position can't be at left of the board
        if dir == Dir.L:
            if freePosition[1] == 0:
                return None
            else:
                new = self.copy()
                temp = new.board[freePosition[0]][freePosition[1]-1]
                new.board[freePosition[0]][freePosition[1]-1] = new.board[freePosition[0]][freePosition[1]]
                new.board[freePosition[0]][freePosition[1]] = temp

        # Free position can't be at right of the board
        if dir == Dir.R:
            if freePosition[1] == 2:
                return None
            else:
                new = self.copy()
                temp = new.board[freePosition[0]][freePosition[1]+1]
                new.board[freePosition[0]][freePosition[1]+1] = new.board[freePosition[0]][freePosition[1]]
                new.board[freePosition[0]][freePosition[1]] = temp

        # Free position can't be at top of the board
        if dir == Dir.U:
            if freePosition[0] == 0:
                return None
            else:
                new = self.copy()
                temp = new.board[freePosition[0]-1][freePosition[1]]
                new.board[freePosition[0]-1][freePosition[1]] = new.board[freePosition[0]][freePosition[1]]
                new.board[freePosition[0]][freePosition[1]] = temp

        # Free position can't be at bottom of the board
        if dir == Dir.D:
            if freePosition[0] == 2:
                return None
            else:
                new = self.copy()
                temp = new.board[freePosition[0]+1][freePosition[1]]
                new.board[freePosition[0]+1][freePosition[1]] = new.board[freePosition[0]][freePosition[1]]
                new.board[freePosition[0]][freePosition[1]] = temp

        return new

    def genChilds(self):
        return self.move(Dir.L), self.move(Dir.U), self.move(Dir.R), self.move(Dir.D)

    def __repr__(self):
        res = ''
        for i in range(3):
            res += '\n'
            for j in range(3):
                res += str(self.board[i][j]) + ' '
        return res
