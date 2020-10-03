from copy import deepcopy
from sys import argv, exit
from memory import Memory
from util import getSettings
from algorithms import optimalAlgorithm, fifo, secondChance, lru

if __name__ == '__main__':
    if len(argv) != 2:
        print('ERRO')
        exit()

    file = open(argv[1], 'r')

    settings = getSettings(file)

    if settings is None:
        exit()

    # memory = Memory(deepcopy(settings[0]), deepcopy(settings[1]))
    # optimalAlgorithm(memory, deepcopy(settings[2]))
    #
    # memory = Memory(deepcopy(settings[0]), deepcopy(settings[1]))
    # fifo(memory, deepcopy(settings[2]))

    # memory = Memory(deepcopy(settings[0]), deepcopy(settings[1]))
    # secondChance(memory, deepcopy(settings[2]))

    memory = Memory(deepcopy(settings[0]), deepcopy(settings[1]))
    lru(memory, deepcopy(settings[2]))

    file.close()

