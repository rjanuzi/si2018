import random
from enum import Enum

class Dir(Enum):
    L = 1
    R = 2
    U = 3
    D = 4

def manhattanDist(a,b):
    sum = 0
    for i in range(len(a)):
        sum += abs(a[i]-b[i])
    return sum

class Puzzle:
    def __init__(self, depth=0):
        pieces = list(range(9))

        random.shuffle(pieces)
        while pieces == [[0,1,2],[3,4,5],[6,7,8]]: # Can't create a resolved board
            random.shuffle(pieces)

        self.depth = depth
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

    def copy(self):
        new = Puzzle()
        new.board = self.board.copy()
        new.depth = self.depth
        return new

    def move(self, dir):
        """Move to a direction (Dir Enum)"""
        freePosition = self.findPiece()

        new = self.copy()
        new.depth = self.depth+1

        # Free position can't be at left of the board
        if dir == Dir.L:
            if freePosition[1] == 0:
                return None
            else:
                temp = new.board[freePosition[0]][freePosition[1]-1]
                new.board[freePosition[0]][freePosition[1]-1] = new.board[freePosition[0]][freePosition[1]]
                new.board[freePosition[0]][freePosition[1]] = temp

        # Free position can't be at right of the board
        if dir == Dir.R:
            if freePosition[1] == 2:
                return None
            else:
                temp = new.board[freePosition[0]][freePosition[1]+1]
                new.board[freePosition[0]][freePosition[1]+1] = new.board[freePosition[0]][freePosition[1]]
                new.board[freePosition[0]][freePosition[1]] = temp

        # Free position can't be at top of the board
        if dir == Dir.U:
            if freePosition[0] == 0:
                return None
            else:
                temp = new.board[freePosition[0]-1][freePosition[1]]
                new.board[freePosition[0]-1][freePosition[1]] = new.board[freePosition[0]][freePosition[1]]
                new.board[freePosition[0]][freePosition[1]] = temp

        # Free position can't be at bottom of the board
        if dir == Dir.D:
            if freePosition[0] == 2:
                return None
            else:
                temp = new.board[freePosition[0]+1][freePosition[1]]
                new.board[freePosition[0]+1][freePosition[1]] = new.board[freePosition[0]][freePosition[1]]
                new.board[freePosition[0]][freePosition[1]] = temp

        return new

    def genChilds(self):
        return self.move(Dir.L), self.move(Dir.U), self.move(Dir.R), self.move(Dir.D)

    def genSolution(self):
        p = Puzzle()
        p.board = [[0,1,2],[3,4,5],[6,7,8]]
        return p

    def getSolutionBoard(self):
        return [[0,1,2],[3,4,5],[6,7,8]]

    def getSolutionBoardPiecesPos(self):
        return {0:[0,0],1:[0,1],2:[0,2],3:[1,0],4:[1,1],5:[1,2],6:[2,0],7:[2,1],8:[2,2],}

    def h1(self):
        """ The idea of this heuristic is to calculate how much pieces are not in the right place."""
        sBoard = self.getSolutionBoard()
        piecesOutOfTheSpot = 0
        for i in range(3):
            for j in range(3):
                if sBoard[i][j] != self.board[i][j]:
                    piecesOutOfTheSpot += 1
        return piecesOutOfTheSpot

    def h2(self):
        """ The idea is to sum the manhattan distance of each piece to the correct position."""
        h = 0
        correctPositions = self.getSolutionBoardPiecesPos()
        for i in range(3):
            for j in range(3):
                h += manhattanDist(correctPositions[self.board[i][j]], [i,j])

        return h

    def h3(self):
        """The idea is to multiply the other two heuristics."""
        return self.h1()*self.h2()

    def __repr__(self):
        # res = 'Depth: %s\n' % self.depth
        res = ''
        for i in range(3):
            res += '\n'
            for j in range(3):
                res += str(self.board[i][j]) + ' '
        return res

    def __eq__(self, other):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != other.board[i][j]:
                    return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)
