from puzzle import Puzzle
from llist import dllist

ITER_LIMIT = 100000
MEMORY_SIZE = 100000

# Execute a Deep Search for the solution opening every possible path
def deepSearch_v1(silent=False, iterLimit=ITER_LIMIT, memorySize = MEMORY_SIZE):
    p = Puzzle()
    maxDepth = 0

    # The list of nodes is accessed using LIFO rule (Deep Search), using the
    # tail of the list to maintain insert/remove as O(1)
    nextNodes = []

    iter = 0
    currentNode = p

    while not currentNode.isDone() and iter <= iterLimit:
        iter += 1

        if maxDepth < currentNode.depth:
            maxDepth = currentNode.depth

        if iter % 1000 == 0:
            if not silent:
                print('\nNodes inspected: %s\nWaiting nodes count: %s\nMax depth: %s' % (iter, len(nextNodes), maxDepth))

        childs = currentNode.genChilds()
        for c in reversed(childs): # I want to check the first child first (Order: L, R, U, D)
            if c: # Ignore None (Invalid solutions)
                nextNodes.append(c)

        currentNode = nextNodes.pop()

    if not silent:
        print('\nStarting node:%s' % p)
        print('Last node evaluated:%s' % currentNode)

    return currentNode.isDone(), len(nextNodes), maxDepth

# Execute a Deep Search for the solution ignoring equals states based on a limited "memory"
def deepSearch_v2(silent=False, iterLimit=ITER_LIMIT, memorySize = MEMORY_SIZE):
    p = Puzzle()
    maxDepth = 0

    # The list of nodes is accessed using LIFO rule (Deep Search), using the
    # tail of the list to maintain insert/remove as O(1)
    nextNodes = []
    memory = dllist()

    iter = 0
    currentNode = p
    while not currentNode.isDone() and iter <= iterLimit:
        iter += 1

        if maxDepth < currentNode.depth:
            maxDepth = currentNode.depth

        if iter % 1000 == 0:
            if not silent:
                print('\nNodes inspected: %s\nWaiting nodes count: %s\nMax depth: %s' % (iter, len(nextNodes), maxDepth))

        if currentNode not in memory:
            memory.append(currentNode)
            if len(memory) > memorySize:
                memory.popleft()

        childs = currentNode.genChilds()
        for c in reversed(childs): # I want to check the first child first (Order: L, R, U, D)
            if c: # Ignore None (Invalid solutions)
                if c not in memory: # Ignore know equals nodes
                    nextNodes.append(c)

        currentNode = nextNodes.pop()

    if not silent:
        print('\nStarting node:%s' % p)
        print('Last node evaluated:%s' % currentNode)

    return currentNode.isDone(), len(nextNodes), maxDepth

# deepSearch_v1()
# deepSearch_v2()
