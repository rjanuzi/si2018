from state import State
from random import choice

def hillClimbing(verbose=True, maxIterations=1000, state=State()):
    currentState = state

    if verbose:
        print('\nStarting: %s\n' % currentState)

    for i in range(maxIterations):
        if currentState.h() == 0:
            break

        if verbose:
            if i % 1000 == 0:
                print('\nIteration %s. h()=%s' % (i, currentState.h()))

        neighbors = currentState.genNeighborsStates()

        neighbors.append(currentState) # Use the current state in the comparison
        bestIndex = 0
        for j in range(1, len(neighbors)):
            if neighbors[j].h() < neighbors[bestIndex].h():
                bestIndex = j

        topH = neighbors[bestIndex].h()
        filteredNeighbors = [n for n in neighbors if n.h()==topH] # If theres elements with same h() as the best, take one randomly
        currentState = choice(filteredNeighbors)

    if verbose or currentState.h() == 0:
        print('\nResult: %s\n' % currentState)

    return currentState.h() == 0


# Tests
successCount = 0
for i in range(100):
    print('\nRunning...%s%%' % i)
    if hillClimbing(verbose=False, maxIterations=10000):
        successCount += 1

print('\n\nSuccess: %s. Fail: %s. Success Rate: %s%%' % (successCount, 100-successCount, successCount))
