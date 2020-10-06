from copy import deepcopy
from sys import argv, exit

import algorithms
import memory
import util

if __name__ == '__main__':
    if len(argv) != 2:
        print('ERRO. Use core.py <settings file>')
        exit()

    file = open(argv[1], 'r')

    settings = util.getSettings(file)
    file.close()

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
