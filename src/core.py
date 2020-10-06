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

    if settings is None:
        exit()

    memory = memory.Memory(deepcopy(settings[0]), deepcopy(settings[1]))
    algorithms.optimalAlgorithm(memory, deepcopy(settings[2]))

    memory.reset(deepcopy(settings[1]))
    algorithms.fifo(memory, deepcopy(settings[2]))

    memory.reset(deepcopy(settings[1]))
    algorithms.secondChance(memory, deepcopy(settings[2]))

    memory.reset(deepcopy(settings[1]))
    algorithms.lru(memory, deepcopy(settings[2]))

    memory.reset(deepcopy(settings[1]))
    algorithms.nru(memory, deepcopy(settings[2]), deepcopy(settings[3]))

    file.close()
