from state import State
from random import choice
from random import random

def genPop(size=1000):
    pop = []
    for i in range(size):
        pop.append(State())
    return pop

def crossover(individual1, individual2):
    cutIndex = int(random()*len(state1.board))
    child1 = State()
    child2 = State()

    child1.board = individual1.board[:cutIndex]+individual2.board[cutIndex:]
    child2.board = individual2.board[:cutIndex]+individual1.board[cutIndex:]

    return [child1, child2]

def selection(pop, percentage = 0.1):
    """ Select in a proporcional roulet """
    howMany = int((len(pop)*percentage))
    selected = []
    fitnessArray = [i.calcFitness() for i in pop]
    totalFitness = sum(fitnessArray)

    for i in range(howMany):
        fitnessProportion = [f/totalFitness for f in fitnessArray]
        acc = 0
        pick = random()
        j = 0
        for j in range(len(fitnessProportion)):
            acc += fitnessProportion[j]
            if pick < acc:
                break
            j += 1
        selected.append(pop[j])

    return selected

def mutation(individual, mutationRate = 0.1):
    # TODO
    return None

def geneticAlgorithm(verbose=True, maxIterations=1000, initialPop=genPop()):
    return None

# Tests
