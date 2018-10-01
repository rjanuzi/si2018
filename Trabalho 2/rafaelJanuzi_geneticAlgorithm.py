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

def crossover(individual1, individual2):
    cutIndex = int(random()*len(individual1.board))
    child1 = State()
    child2 = State()

    child1.board = individual1.board[:cutIndex]+individual2.board[cutIndex:]
    child2.board = individual2.board[:cutIndex]+individual1.board[cutIndex:]

    mutation(child1, mutationRate=MUTATION_RATE)
    mutation(child2, mutationRate=MUTATION_RATE)

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
        if i > len(pop):
            return saved
        fitnessArray = [i.calcFitness() for i in pop]
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

def geneticAlgorithm(verbose=True, maxIterations=MAX_ITERATIONS, pop=genPop(size=POP_SIZE), elitismRate=ELITISM_RATE):

    for i in range(maxIterations):
        newPop = []

        if verbose:
            print('\nStarting epoch %s' % i)

        individualsToCrossOver = selection(pop=pop, percentage=CROSSOVER_PERCENTAGE)

        # Crossovers
        while len(individualsToCrossOver) >= 2:
            parent1 = individualsToCrossOver.pop(int(random()*len(individualsToCrossOver)))
            parent2 = individualsToCrossOver.pop(int(random()*len(individualsToCrossOver)))
            childs = crossover(parent1, parent2)
            pop.append(childs[0])
            pop.append(childs[1])

        if verbose:
            print('Pop size after crossover: %s' % len(pop))

        # Sort to facilitate
        pop.sort(key=lambda x: x.calcFitness(), reverse=True)

        if verbose:
            print('Top fitness: %s' % pop[0].calcFitness())

        # Save the elit
        howManyForElitism = int(elitismRate*POP_SIZE)
        for j in range(howManyForElitism):
            newPop.append(pop.pop(j))

        # Save the rest based on a proportional roulet
        newPop += save(pop=pop, howMany=POP_SIZE-howManyForElitism)
        pop = newPop

    pop.sort(key=lambda x: x.calcFitness(), reverse=True)
    print('\n\nEvolution end.\nTop individual: %s' % pop[0])

# Tests
geneticAlgorithm()
