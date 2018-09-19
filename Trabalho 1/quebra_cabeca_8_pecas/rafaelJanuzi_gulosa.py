from puzzle import Puzzle
from llist import dllist
import random

ITER_LIMIT = 10000000
MEMORY_SIZE = 100000

def greedySearch_v1():
    p = Puzzle()
    maxDepth = 0
    maxQuality = 0

    iter = 0
    currentNode = p
    currentQuality = p.qualityMes01()

    while currentNode and not currentNode.isDone() and iter <= ITER_LIMIT:
        iter += 1

        if maxDepth < currentNode.depth:
            maxDepth = currentNode.depth

        if maxQuality < currentQuality:
            maxQuality = currentQuality

        if iter % 1000 == 0:
            print('\nNodes inspected: %s\nMax depth: %s\nMax quality: %s\nLast Quality: %s' % (iter, maxDepth, maxQuality, currentQuality))

        childs = currentNode.genChilds()
        bestChild = None
        currentNode = None
        for c in childs:
            if c: # Ignore None (Invalid solutions)
                if not bestChild:
                    bestChild = c
                else:
                    if bestChild.qualityMes01() < c.qualityMes01():
                        bestChild = c

        currentNode = bestChild
        currentQuality = currentNode.qualityMes01()

    print('\nStarting node:%s' % p)
    print('Last node evaluated:%s\nQuality: %s' % (currentNode, currentNode.qualityMes01()))

def greedySearch_v2():
    p = Puzzle()
    maxDepth = 0
    maxQuality = 0

    memory = dllist()

    iter = 0
    currentNode = p
    currentQuality = p.qualityMes01()

    while currentNode and not currentNode.isDone() and iter <= ITER_LIMIT:
        iter += 1

        if maxDepth < currentNode.depth:
            maxDepth = currentNode.depth

        if maxQuality < currentQuality:
            maxQuality = currentQuality

        if currentNode not in memory:
            memory.append(currentNode)
            if len(memory) > MEMORY_SIZE:
                memory.popleft()

        if iter % 100 == 0:
            print('\nNodes inspected: %s\nMax depth: %s\nMax quality: %s\nLast Quality: %s' % (iter, maxDepth, maxQuality, currentQuality))

        childs = currentNode.genChilds()
        childs = [x for x in childs if x is not None] # Remove None childs

        bestChild = None
        currentNode = None
        for c in childs:
            if c not in memory: # Ignore c if it is in memory
                if not bestChild:
                    bestChild = c
                else:
                    if bestChild.qualityMes01() < c.qualityMes01():
                        bestChild = c

        if not bestChild: # If all childs are in memory, chose one randomly
            bestChild = random.choice(childs)

        currentNode = bestChild
        currentQuality = currentNode.qualityMes01()

    print('\nStarting node:%s' % p)
    print('Last node evaluated:%s\nQuality: %s' % (currentNode, currentNode.qualityMes01()))

greedySearch_v1()
# greedySearch_v2()
