from copy import deepcopy
from sys import argv, exit

import algorithms
import memory
import util
import matplotlib.pyplot as plt


if __name__ == '__main__':
    settings = []
    if len(argv) == 3 and argv[1] == '-f':
        file = open(argv[2], 'r')
        settings = util.getSettings(file)
        file.close()
    elif len(argv) == 4 and argv[1] == '-g':
        settings = util.generateSettings(int(argv[2]), int(argv[3]))
    else:
        print('ERROR. Use core.py <settings file>')
        exit()

    if settings is None:
        exit()

    memory = memory.Memory(deepcopy(settings[0]), deepcopy(settings[1]))
    optimalAlgorith = algorithms.optimalAlgorithm(memory, deepcopy(settings[2]))

    memory.reset(deepcopy(settings[1]))
    fifo = algorithms.fifo(memory, deepcopy(settings[2]))

    memory.reset(deepcopy(settings[1]))
    secondChance = algorithms.secondChance(memory, deepcopy(settings[2]))

    memory.reset(deepcopy(settings[1]))
    lru = algorithms.lru(memory, deepcopy(settings[2]))

    memory.reset(deepcopy(settings[1]))
    nru = algorithms.nru(memory, deepcopy(settings[2]), deepcopy(settings[3]))

    print('Results:\n')
    print('\tOptimal Algorith: ', optimalAlgorith, ' faults.')
    print('\tFIFO: ', fifo, ' faults.')
    print('\tSecond Chance: ', secondChance, ' faults.')
    print('\tLRU: ', lru, ' faults.')
    print('\tNRU: ', nru, ' faults.')

    # plt.bar(['Optimal Algorith', 'FIFO', 'Second Chance', 'LRU', 'NRU'], [optimalAlgorith, fifo, secondChance, lru, nru])
    # plt.ylabel('Algorithms')
    # plt.show()
