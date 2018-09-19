from puzzle import Puzzle
from llist import dllist

ITER_LIMIT = 100000
MEMORY_SIZE = 100000

# Execute a Width Search for the solution opening every possible path
def widthSearch_v1():
    p = Puzzle()

    nextNodes = dllist() # Using linked list to execute FIFO in O(1)
    maxDepth = 0
    iter = 0
    currentNode = p

    while not currentNode.isDone() and iter <= ITER_LIMIT:
        iter += 1

        if maxDepth < currentNode.depth:
            maxDepth = currentNode.depth

        if iter % 1000 == 0:
            print('Nodes inspected: %s\nWaiting nodes count: %s\nMax depth: %s' % (iter, len(nextNodes), maxDepth))

        childs = currentNode.genChilds()
        for c in reversed(childs): # I want to check the first child first (Order: L, R, U, D)
            if c: # Ignore None (Invalid solutions)
                nextNodes.append(c)

        currentNode = nextNodes.popleft()

    print('\nStarting node:%s' % p)
    print('Last node evaluated:%s' % currentNode)

# Execute a Deep Search for the solution ignoring equals states based on a limited "memory"
def widthSearch_v2():
    p = Puzzle()

    nextNodes = dllist()
    memory = dllist()

    maxDepth = 0
    iter = 0
    currentNode = p
    while not currentNode.isDone() and iter <= ITER_LIMIT:
        iter += 1

        if maxDepth < currentNode.depth:
            maxDepth = currentNode.depth

        if iter % 1000 == 0:
            print('\nNodes inspected: %s\nWaiting nodes count: %s\nMax depth: %s' % (iter, len(nextNodes), maxDepth))

        if currentNode not in memory:
            memory.append(currentNode)
            if len(memory) > MEMORY_SIZE:
                memory.popleft()

        childs = currentNode.genChilds()
        for c in reversed(childs): # I want to check the first child first (Order: L, R, U, D)
            if c: # Ignore None (Invalid solutions)
                if c not in memory: # Ignore know equals nodes
                    nextNodes.append(c)

        currentNode = nextNodes.popleft()

    print('\nStarting node:%s' % p)
    print('Last node evaluated:%s' % currentNode)

# widthSearch_v1()
widthSearch_v2()
