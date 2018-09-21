from puzzle import Puzzle
from llist import dllist
import random

ITER_LIMIT = 100000
MEMORY_SIZE = 100

def greedySearch_h1_v1(silent=False, iterLimit=ITER_LIMIT, memorySize = MEMORY_SIZE):
    p = Puzzle()
    maxDepth = 0
    minH = 10

    iter = 0
    currentNode = p
    currentH = p.h1()

    while currentNode and not currentNode.isDone() and iter <= iterLimit:
        iter += 1

        if maxDepth < currentNode.depth:
            maxDepth = currentNode.depth

        if minH > currentH:
            minH = currentH

        if iter % 1000 == 0:
            if not silent:
                print('\nNodes inspected: %s\nMax depth: %s\nMin H(): %s\nLast H(): %s' % (iter, maxDepth, minH, currentH))

        childs = currentNode.genChilds()
        bestChild = None
        currentNode = None
        for c in childs:
            if c: # Ignore None (Invalid solutions)
                if not bestChild:
                    bestChild = c
                else:
                    if bestChild.h1() > c.h1():
                        bestChild = c

        currentNode = bestChild
        currentQuality = currentNode.h1()

    if not silent:
        print('\nStarting node:%s' % p)
        print('Last node evaluated:%s\nH(): %s' % (currentNode, currentNode.h1()))

    return currentNode.isDone(), minH, maxDepth

def greedySearch_h1_v2(silent=False, iterLimit=ITER_LIMIT, memorySize = MEMORY_SIZE):
    p = Puzzle()
    maxDepth = 0
    minH = 10

    memory = dllist()

    iter = 0
    currentNode = p
    currentH = p.h1()

    while currentNode and not currentNode.isDone() and iter <= iterLimit:
        iter += 1

        if maxDepth < currentNode.depth:
            maxDepth = currentNode.depth

        if minH > currentH:
            minH = currentH

        if currentNode not in memory:
            memory.append(currentNode)
            if len(memory) > memorySize:
                memory.popleft()

        if iter % 100 == 0:
            if not silent:
                print('\nNodes inspected: %s\nMax depth: %s\nMin H(): %s\nLast H(): %s' % (iter, maxDepth, minH, currentH))

        childs = currentNode.genChilds()
        childs = [x for x in childs if x is not None] # Remove None childs

        bestChild = None
        currentNode = None
        for c in childs:
            if c not in memory: # Ignore c if it is in memory
                if not bestChild:
                    bestChild = c
                else:
                    if bestChild.h1() > c.h1():
                        bestChild = c

        if not bestChild: # If all childs are in memory, chose one randomly
            bestChild = random.choice(childs)

        currentNode = bestChild
        currentH = currentNode.h1()

    if not silent:
        print('\nStarting node:%s' % p)
        print('Last node evaluated:%s\nH(): %s' % (currentNode, currentNode.h1()))

    return currentNode.isDone(), minH, maxDepth

def greedySearch_h2_v1(silent=False, iterLimit=ITER_LIMIT, memorySize = MEMORY_SIZE):
    p = Puzzle()
    maxDepth = 0
    minH = 10

    iter = 0
    currentNode = p
    currentH = p.h2()

    while currentNode and not currentNode.isDone() and iter <= iterLimit:
        iter += 1

        if maxDepth < currentNode.depth:
            maxDepth = currentNode.depth

        if minH > currentH:
            minH = currentH

        if iter % 1000 == 0:
            if not silent:
                print('\nNodes inspected: %s\nMax depth: %s\nMin H(): %s\nLast H(): %s' % (iter, maxDepth, minH, currentH))

        childs = currentNode.genChilds()
        bestChild = None
        currentNode = None
        for c in childs:
            if c: # Ignore None (Invalid solutions)
                if not bestChild:
                    bestChild = c
                else:
                    if bestChild.h2() > c.h2():
                        bestChild = c

        currentNode = bestChild
        currentQuality = currentNode.h2()

    if not silent:
        print('\nStarting node:%s' % p)
        print('Last node evaluated:%s\nH(): %s' % (currentNode, currentNode.h2()))

    return currentNode.isDone(), minH, maxDepth

def greedySearch_h2_v2(silent=False, iterLimit=ITER_LIMIT, memorySize = MEMORY_SIZE):
    p = Puzzle()
    maxDepth = 0
    minH = 10

    memory = dllist()

    iter = 0
    currentNode = p
    currentH = p.h2()

    while currentNode and not currentNode.isDone() and iter <= iterLimit:
        iter += 1

        if maxDepth < currentNode.depth:
            maxDepth = currentNode.depth

        if minH > currentH:
            minH = currentH

        if currentNode not in memory:
            memory.append(currentNode)
            if len(memory) > memorySize:
                memory.popleft()

        if iter % 100 == 0:
            if not silent:
                print('\nNodes inspected: %s\nMax depth: %s\nMin H(): %s\nLast H(): %s' % (iter, maxDepth, minH, currentH))

        childs = currentNode.genChilds()
        childs = [x for x in childs if x is not None] # Remove None childs

        bestChild = None
        currentNode = None
        for c in childs:
            if c not in memory: # Ignore c if it is in memory
                if not bestChild:
                    bestChild = c
                else:
                    if bestChild.h2() > c.h2():
                        bestChild = c

        if not bestChild: # If all childs are in memory, chose one randomly
            bestChild = random.choice(childs)

        currentNode = bestChild
        currentH = currentNode.h2()

    if not silent:
        print('\nStarting node:%s' % p)
        print('Last node evaluated:%s\nH(): %s' % (currentNode, currentNode.h2()))

    return currentNode.isDone(), minH, maxDepth

def greedySearch_h3_v1(silent=False, iterLimit=ITER_LIMIT, memorySize = MEMORY_SIZE):
    p = Puzzle()
    maxDepth = 0
    minH = 10

    iter = 0
    currentNode = p
    currentH = p.h3()

    while currentNode and not currentNode.isDone() and iter <= iterLimit:
        iter += 1

        if maxDepth < currentNode.depth:
            maxDepth = currentNode.depth

        if minH > currentH:
            minH = currentH

        if iter % 1000 == 0:
            if not silent:
                print('\nNodes inspected: %s\nMax depth: %s\nMin H(): %s\nLast H(): %s' % (iter, maxDepth, minH, currentH))

        childs = currentNode.genChilds()
        bestChild = None
        currentNode = None
        for c in childs:
            if c: # Ignore None (Invalid solutions)
                if not bestChild:
                    bestChild = c
                else:
                    if bestChild.h3() > c.h3():
                        bestChild = c

        currentNode = bestChild
        currentQuality = currentNode.h3()

    if not silent:
        print('\nStarting node:%s' % p)
        print('Last node evaluated:%s\nH(): %s' % (currentNode, currentNode.h3()))

    return currentNode.isDone(), minH, maxDepth

def greedySearch_h3_v2(silent=False, iterLimit=ITER_LIMIT, memorySize = MEMORY_SIZE):
    p = Puzzle()
    maxDepth = 0
    minH = 10

    memory = dllist()

    iter = 0
    currentNode = p
    currentH = p.h3()

    while currentNode and not currentNode.isDone() and iter <= iterLimit:
        iter += 1

        if maxDepth < currentNode.depth:
            maxDepth = currentNode.depth

        if minH > currentH:
            minH = currentH

        if currentNode not in memory:
            memory.append(currentNode)
            if len(memory) > memorySize:
                memory.popleft()

        if iter % 100 == 0:
            if not silent:
                print('\nNodes inspected: %s\nMax depth: %s\nMin H(): %s\nLast H(): %s' % (iter, maxDepth, minH, currentH))

        childs = currentNode.genChilds()
        childs = [x for x in childs if x is not None] # Remove None childs

        bestChild = None
        currentNode = None
        for c in childs:
            if c not in memory: # Ignore c if it is in memory
                if not bestChild:
                    bestChild = c
                else:
                    if bestChild.h3() > c.h3():
                        bestChild = c

        if not bestChild: # If all childs are in memory, chose one randomly
            bestChild = random.choice(childs)

        currentNode = bestChild
        currentH = currentNode.h3()

    if not silent:
        print('\nStarting node:%s' % p)
        print('Last node evaluated:%s\nH(): %s' % (currentNode, currentNode.h3()))

    return currentNode.isDone(), minH, maxDepth

# greedySearch_h1_v1()
# greedySearch_h1_v2()
# greedySearch_h2_v2()
# greedySearch_h2_v2()
# greedySearch_h3_v1()
# greedySearch_h3_v2()
