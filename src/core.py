from sys import argv, exit
from memory.core import Memory
from util.core import getSettings


if __name__ == '__main__':
    if len(argv) != 2:
        print('ERRO')
        exit()

    file = open(argv[1], 'r')

    settings = getSettings(file)

    if settings is None:
        exit()

    memory = Memory(settings[0], settings[1])

    file.close()

