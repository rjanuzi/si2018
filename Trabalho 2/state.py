from random import random

class State:
    def __init__(self, depth=0):
        self.board = [int(num*random()*8) for num in [1]*8]

    def h(self):
        """ Counts the number of queens that attack each other. """
        attacks = 0

        # Count in vertical
        for i in range(8):
            for j in range(i+1, 8):
                if self.board[i] == self.board[j]:
                    attacks += 1

        # Count in diagonals
        for i in range(8):
            acc = 0
            for j in range(i+1, 8):
                acc += 1
                supPos = self.board[i]-acc # Next queen can't be at this position in the ascendent diagonal
                infPos = self.board[i]+acc # Next queen can't be at this position in the descendent diagonal
                if supPos > 0 and self.board[j] == supPos:
                    attacks += 1
                if infPos < 8 and self.board[j] == infPos:
                    attacks += 1

        return attacks

    def genNeighborsStates(self):
        neighborsLst = []

        # Gen the neighbors state list
        for i in range(8):
            if self.board[i] > 0: # Queen goes up in line i
                c = self.clone()
                c.board[i] -= 1
                neighborsLst.append(c)
            if self.board[i] < 7: # Queen goes down in line i
                c = self.clone()
                c.board[i] += 1
                neighborsLst.append(c)

        return neighborsLst

    def clone(self):
        c = State()
        c.board = self.board.copy()
        return c

    def __repr__(self):
        res = '\nArray:%s\nMatrix:\n' % self.board
        for i in range(8):
            res += '\n'
            for j in range(8):
                if self.board[j] == i:
                    res += ' 1 '
                else:
                    res += ' 0 '
        return res+'\nh() = %s'%self.h()

    def __eq__(self, other):
        return self.board==other.board

    def __ne__(self, other):
        return not self.__eq__(other)
