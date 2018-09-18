from puzzle import Puzzle
# from llist import dllist

ITER_LIMIT = 100000
MEMORY_SIZE = 250

# Execute a Width Search for the solution opening every possible path
def widthSearch_v1():
    p = Puzzle()
    maxDepth = 0

    # The list of nodes is accessed using LIFO rule (Deep Search), but using the
    # tail of the list to maintain insert/remove as O(1)
    # nextNodes = [p]
    nextNodes = dllist()

    iter = 0
    # currentNode = nextNodes.pop()
    currentNode = nextNodes.popleft()

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

        # currentNode = nextNodes.pop(0)
        currentNode = nextNodes.popleft()

    print('\nStarting node:%s' % p)
    print('Last node evaluated:%s' % currentNode)

# Execute a Deep Search for the solution ignoring equals states based on a limited "memory"
def widthSearch_v2():
    p = Puzzle()
    maxDepth = 0

    # The list of nodes is accessed using FIFO rule (Deep Search), but using the
    # tail of the list to maintain insert/remove as O(1)
    nextNodes = [p]
    memory = [p]

    iter = 0
    currentNode = nextNodes.pop()
    while not currentNode.isDone() and iter <= ITER_LIMIT:
        iter += 1

        if maxDepth < currentNode.depth:
            maxDepth = currentNode.depth

        if iter % 1000 == 0:
            print('\nNodes inspected: %s\nWaiting nodes count: %s\nMax depth: %s' % (iter, len(nextNodes), maxDepth))

        if currentNode not in memory:
            memory.append(currentNode)
            if len(memory) > MEMORY_SIZE:
                memory.pop(0)

        childs = currentNode.genChilds()
        for c in reversed(childs): # I want to check the first child first (Order: L, R, U, D)
            if c: # Ignore None (Invalid solutions)
                if c not in memory: # Ignore know equals nodes
                    nextNodes.append(c)

        currentNode = nextNodes.pop(0)

    print('\nStarting node:%s' % p)
    print('Last node evaluated:%s' % currentNode)

# widthSearch_v1()
widthSearch_v2()
