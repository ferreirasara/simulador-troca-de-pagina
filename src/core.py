from copy import deepcopy
from sys import argv, exit

import algorithms
import memory
import util
import time
import timeit
import matplotlib.pyplot as plt


if __name__ == '__main__':
    settings = []
    if len(argv) == 3 and argv[1] == '-f':
        file = open(argv[2], 'r')
        settings = util.getSettings(file)
        file.close()
    elif len(argv) == 5 and argv[1] == '-g':
        settings = util.generateSettings(int(argv[2]), int(argv[3]), int(argv[4]))
    elif len(argv) == 6 and argv[1] == '-g':
        settings = util.generateSettings(int(argv[2]), int(argv[3]), int(argv[4]), str(argv[5]))
    else:
        print('ERROR. Use core.py <settings file>')
        exit()

    if settings is None:
        exit()

    print(settings)

    memory = memory.Memory(deepcopy(settings[0]), deepcopy(settings[1]))
    startOptimalAlgorithm = time.perf_counter_ns()
    optimalAlgorith = algorithms.optimalAlgorithm(memory, deepcopy(settings[2]))
    endOptimalAlgorithm = time.perf_counter_ns()
    timeOptimalAlgorithm = (endOptimalAlgorithm - startOptimalAlgorithm)

    memory.reset(deepcopy(settings[1]))
    startFifo = time.perf_counter_ns()
    fifo = algorithms.fifo(memory, deepcopy(settings[2]))
    endFifo = time.perf_counter_ns()
    timeFifo = (endFifo - startFifo)

    memory.reset(deepcopy(settings[1]))
    startSecondChance = time.perf_counter_ns()
    secondChance = algorithms.secondChance(memory, deepcopy(settings[2]))
    endSecondChance = time.perf_counter_ns()
    timeSecondChance = (endSecondChance - startSecondChance)

    memory.reset(deepcopy(settings[1]))
    startLRU = time.perf_counter_ns()
    lru = algorithms.lru(memory, deepcopy(settings[2]))
    endLRU = time.perf_counter_ns()
    timeLRU = (endLRU - startLRU)

    memory.reset(deepcopy(settings[1]))
    startNRU = time.perf_counter_ns()
    nru = algorithms.nru(memory, deepcopy(settings[2]), deepcopy(settings[3]))
    endNRU = time.perf_counter_ns()
    timeNRU = (endNRU - startNRU)

    print('Results:\n')
    print('\tOptimal Algorith: ', optimalAlgorith, ' faults.\tExecution Time: ', timeOptimalAlgorithm, ' ns')
    print('\tFIFO: ', fifo, ' faults.\t\tExecution Time: ', timeFifo, ' ns')
    print('\tSecond Chance: ', secondChance, ' faults.\tExecution Time: ', timeSecondChance, ' ns')
    print('\tLRU: ', lru, ' faults.\t\tExecution Time: ', timeLRU, ' ns')
    print('\tNRU: ', nru, ' faults.\t\tExecution Time: ', timeNRU, ' ns')

    plt.bar(['Optimal Algorith', 'FIFO', 'Second Chance', 'LRU', 'NRU'], [timeOptimalAlgorithm, timeFifo, timeSecondChance, timeLRU, timeNRU])
    plt.xlabel('Algorithms')
    plt.ylabel('Nanoseconds')
    plt.show()
