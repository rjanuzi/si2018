from state import State
from random import choice
from random import random

POP_SIZE = 100 # Fixed population size
MAX_ITERATIONS = 1000 # Algorithm max iterations
CROSSOVER_PERCENTAGE = 1.0 # How much elements are selected for crossover (One individual can be selected multiple times)
MUTATION_RATE = 0.1 # The mutation probability for a new individual
ELITISM_RATE = 0.1 # Proportion of the population selected by the top fitness

def genPop(size=1000):
    pop = []
    for i in range(size):
        pop.append(State())
    return pop

def mutation(individual, mutationRate=0.1):
    # Change an random queen to a random position with a probability of <mutationRate>
    if random() <= mutationRate:
        individual.board[int(random()*len(individual.board))] = int(random()*8)
        return True

def crossover(individual1, individual2, mutationRate=MUTATION_RATE):
    cutIndex = int(random()*len(individual1.board))
    child1 = State()
    child2 = State()

    child1.board = individual1.board[:cutIndex]+individual2.board[cutIndex:]
    child2.board = individual2.board[:cutIndex]+individual1.board[cutIndex:]

    mutation(child1, mutationRate=mutationRate)
    mutation(child2, mutationRate=mutationRate)

    return [child1, child2]

def selection(pop, percentage=0.1):
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

def save(pop, howMany):
    """ Select individuals to save in a proporcional roulet """
    saved = []

    for i in range(howMany):
        if len(pop) <= 0:
            return saved
        fitnessArray = [ind.calcFitness() for ind in pop]
        totalFitness = sum(fitnessArray)
        fitnessProportion = [f/totalFitness for f in fitnessArray]
        acc = 0
        pick = random()
        j = 0
        for j in range(len(fitnessProportion)):
            acc += fitnessProportion[j]
            if pick < acc:
                break
            j += 1
        saved.append(pop.pop(j))

    return saved

def geneticAlgorithm(verbose=True, maxIterations=MAX_ITERATIONS, popSize=POP_SIZE,
    elitismRate=ELITISM_RATE, crossOverPercentage=CROSSOVER_PERCENTAGE, mutationRate=MUTATION_RATE):

    currentEpoch = 1
    pop = genPop(popSize)

    for i in range(maxIterations):
        if verbose:
            print('\nStarting epoch %s' % i)

        individualsToCrossOver = selection(pop=pop, percentage=crossOverPercentage)

        # Crossovers
        while len(individualsToCrossOver) >= 2:
            parent1 = individualsToCrossOver.pop(int(random()*len(individualsToCrossOver)))
            parent2 = individualsToCrossOver.pop(int(random()*len(individualsToCrossOver)))
            childs = crossover(parent1, parent2, mutationRate=mutationRate)
            pop.append(childs[0])
            pop.append(childs[1])

        if verbose:
            print('Pop size after crossover: %s' % len(pop))

        # Sort to facilitate
        pop.sort(key=lambda x: x.calcFitness(), reverse=False)

        # Check if theres a solution
        if pop[-1].h() == 0:
            break

        if verbose:
            print('Top fitness: %s' % pop[-1].calcFitness())

        # Save the elit
        howManyForElitism = int(elitismRate*popSize)
        savedByElitism = []
        for j in range(howManyForElitism):
            savedByElitism.append(pop.pop())

        if verbose:
            print('Saved by elitism: %s (%s)' % (howManyForElitism, len(savedByElitism)))

        # Save the rest based on a proportional roulet
        savedByLuck = save(pop=pop, howMany=popSize-howManyForElitism)
        if verbose:
            print('Saved by luck (based on fitness): %s (%s)' % ((popSize-howManyForElitism), len(savedByLuck)))

        pop = savedByElitism + savedByLuck

        if verbose:
            print('Total saved: %s' % len(pop))

        currentEpoch += 1

    if verbose:
        pop.sort(key=lambda x: x.calcFitness(), reverse=False)
        print('\n\nEvolution end. (Epochs: %s)\nTop individual: %s' % (currentEpoch, pop[-1]))

    if pop[-1].h() == 0:
        return True
    return False

# Tests
# geneticAlgorithm(verbose=True, popSize=10, maxIterations=10, crossOverPercentage=0.1, mutationRate=0.01, elitismRate=0.2)

popSizeVals = [10, 100]
maxIterationsVals = [100, 1000]
crossOverPercentageVals = [0.5, 1.0]
mutationRateVals = [0.05, 0.1, 0.3, 0.5]
elitismRateVals = [0.0, 0.1, 0.3, 0.5]

for s in popSizeVals:
    for maxI in maxIterationsVals:
        for c in crossOverPercentageVals:
            for m in mutationRateVals:
                for e in elitismRateVals:
                    successCount = 0
                    for i in range(100):
                        if geneticAlgorithm(verbose=False, popSize=s, maxIterations=maxI,
                            crossOverPercentage=c, mutationRate=m, elitismRate=e):
                            successCount += 1
                    print('PopSize: %s, Max Iterations: %s, CrossOverPercentage: %s, mutationRate: %s, elitismRate: %s = %s%%' % (s,maxI,c,m,e,successCount))

# def findRandomly():
#     for i in range(1000000):
#         p = State()
#         if p.h() == 0:
#             return True
#     return False
#
# successCount = 0
# for i in range(100):
#     if findRandomly():
#         successCount += 1
# print('Success rate randomly: %s%%' % successCount)
