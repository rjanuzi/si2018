from rafaelJanuzi_profundidade import deepSearch_v1
from rafaelJanuzi_profundidade import deepSearch_v2
from rafaelJanuzi_largura import widthSearch_v1
from rafaelJanuzi_largura import widthSearch_v2
from rafaelJanuzi_gulosa import greedySearch_h1_v1
from rafaelJanuzi_gulosa import greedySearch_h1_v2
from rafaelJanuzi_gulosa import greedySearch_h2_v1
from rafaelJanuzi_gulosa import greedySearch_h2_v2
from rafaelJanuzi_gulosa import greedySearch_h3_v1
from rafaelJanuzi_gulosa import greedySearch_h3_v2

import time

iterations = [1000, 10000]
memorySize = 200

def testTemplate(fun, guloso=False):
    for iteration in iterations:
        success = 0.0
        totalTime = 0.0
        totalWaitingNodes = 0.0
        totalMaxDepth = 0.0
        for i in range(100):
            start = time.time()

            result, waitingNodes, maxDepth = fun(silent=True, iterLimit=iteration, memorySize=memorySize)

            totalTime += (time.time()-start)
            totalWaitingNodes += waitingNodes
            totalMaxDepth += maxDepth

            if result:
                success += 1.0

        if not guloso:
            print('\n=======================================\nIterations Limit: %s\nSuccess rate: %s %%\nAverage exec. time: %s\nAverage waiting nodes: %s\nAverage max depth: %s\n=======================================' % \
            (iteration, success, (totalTime/100.0), (totalWaitingNodes/100.0), (totalMaxDepth/100.0)))
        else:
            print('\n=======================================\nIterations Limit: %s\nSuccess rate: %s %%\nAverage exec. time: %s\nAverage min H(): %s\nAverage max depth: %s\n=======================================' % \
            (iteration, success, (totalTime/100.0), (totalWaitingNodes/100.0), (totalMaxDepth/100.0)))

##################################################################################################
#                                   EXECUTION
##################################################################################################

print('\nTesting deepSearch_v1()')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
testTemplate(fun=deepSearch_v1)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('\nTesting deepSearch_v2()')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
testTemplate(fun=deepSearch_v2)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('\nTesting widthSearch_v1()')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
testTemplate(fun=widthSearch_v1)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('\nTesting widthSearch_v2()')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
testTemplate(fun=widthSearch_v2)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('\nTesting greedySearch_h1_v1()')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
testTemplate(fun=greedySearch_h1_v1, guloso=True)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('\nTesting greedySearch_h1_v2()')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
testTemplate(fun=greedySearch_h1_v2, guloso=True)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('\nTesting greedySearch_h2_v1()')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
testTemplate(fun=greedySearch_h2_v1, guloso=True)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('\nTesting greedySearch_h2_v2()')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
testTemplate(fun=greedySearch_h2_v2, guloso=True)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('\nTesting greedySearch_h3_v1()')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
testTemplate(fun=greedySearch_h3_v1, guloso=True)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('\nTesting greedySearch_h3_v2()')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
testTemplate(fun=greedySearch_h3_v2, guloso=True)
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('\n\nDone.')
