from random import randint, choice
import string
import time


def generateProcessName():
    """
    This function generate two random letters.

    :return: A string with two letters, for a name of process
    :rtype: str
    """
    letters = string.ascii_lowercase
    return ''.join(choice(letters) for i in range(2))


def generateSettings(lenght, totalProcess, numberOfDifferentProcesses, saveToFile=''):
    """
    This function receives the lenght of memory and total of process that will run, and return a list with configurations to simulator.

    :param lenght: lenght of memory.
    :type lenght: int
    :param totalProcess: quantity of processes.
    :type totalProcess: int
    :param numberOfDifferentProcesses: number of different processes.
    :type numberOfDifferentProcesses: int
    :param saveToFile: save to file? Default: no.
    :type saveToFile: str
    :return: list with configurations
    :rtype: tuple[int, list[str], list[str], list[str]]
    """
    saveToFile = saveToFile.lower()
    if saveToFile == '-s':
        file = open(str('settings'+str(time.time())+'.txt'), 'w')
    processes = [[generateProcessName(), False] for i in range(numberOfDifferentProcesses)]
    numberOfDifferentProcesses -= 1
    initialState = []
    processQueue = []
    processAction = []

    for process in range(lenght):
        if randint(0, 10) == 1:
            initialState.append('0')
        else:
            process = processes[randint(0, numberOfDifferentProcesses)]
            while process[1]:
                process = processes[randint(0, numberOfDifferentProcesses)]
            process[1] = True
            initialState.append(process[0])
    for i in range(totalProcess):
        if randint(0, 10) == 1:
            processQueue.append('|')
            processAction.append('|')
        else:
            processQueue.append(processes[randint(0, numberOfDifferentProcesses)][0])
            processAction.append('R' if randint(0, 1) == 0 else 'W')

    if saveToFile == '-s':
        file.write(str(lenght)+'\n')
        file.write(','.join(initialState)+'\n')
        file.write(','.join(processQueue)+'\n')
        file.write(','.join(processAction)+'\n')
        file.close()
    return lenght, initialState, processQueue, processAction


def getSettings(file):
    """
    This function receives a file, process and validate information, and finally return a list with configurations to simulator.

    :param file: a file open previously.
    :type file: TextWrapper
    :return: list with configurations
    :rtype: tuple[int, list[str], list[str], list[str]]
    """
    lines = [line.strip() for line in file]
    if len(lines) < 4:
        print('ERROR - Invalid number of lines.')
        return None

    lenght = lines[0]
    initialState = lines[1].split(',')
    processQueue = lines[2].split(',')
    processAction = lines[3].split(',')

    if lenght.isdigit():
        lenght = int(lenght)
        if lenght > 0:
            if len(initialState) == lenght:
                if len(processQueue) == len(processAction):
                    if '0' not in processQueue:
                        return lenght, initialState, processQueue, processAction
                    else:
                        print('ERROR - The digit 0 must not be used.')
                else:
                    print('ERROR - The process queue and the action list must be the same size.')
            else:
                print('ERROR - The initial state must be the same size as the memory.')
        else:
            print('ERROR - The memory size must be greater than zero.')
    else:
        print('ERROR - Memory size must be a number.')


def setValueInLRUMatrix(matrix, index):
    """
    Set line equal to 1, and column equal to 0.

    :param matrix: a matrix created by LRU algorithm.
    :param index: index for line and column.
    :type matrix: list[list[int]]
    :type index: int
    """
    for i in range(len(matrix)):
        matrix[index][i] = 1

    for i in range(len(matrix)):
        matrix[i][index] = 0


def getMinorValueLRUMatrix(matrix):
    """
    Get index of minor value (process that is the longest unused).

    :param matrix: a matrix created by LRU algorithm.
    :type matrix: list[list[int]]
    :return index if minor value.
    :rtype: int
    """
    minorValue = [0, 999999]
    for i in range(len(matrix)):
        if matrix[i][-1] <= minorValue[1]:
            minorValue[0] = i
            minorValue[1] = matrix[i][-1]
    return minorValue[0]


def calcLRUMatrixValue(matrix):
    """
    Calculates the process usage time.

    :param matrix: a matrix created by LRU algorithm.
    :type matrix: list[list[int]]
    """
    for line in matrix:
        binary = ''.join([str(n) for n in line[:-1]])
        line[-1] = int(binary, 2)


def calcClassOfNRUProcesses(processesClass):
    """
    Calculates the class of the processes.

    :param processesClass: a list created by NRU algorithm.
    :type processesClass: list[list[int]]
    """
    for line in processesClass:
        binary = ''.join([str(line[1]), str(line[2])])
        line[3] = int(binary, 2)


def getMinorClassNRU(processesClass):
    """
    Get index of minor value class.

    :param processesClass: a list created by NRU algorithm.
    :type processesClass: list[list[int]]
    :return index if minor value.
    :rtype: int
    """
    minorValue = [0, 999999]
    for i in range(len(processesClass)):
        if processesClass[i][-1] <= minorValue[1]:
            minorValue[0] = i
            minorValue[1] = processesClass[i][-1]
    return minorValue[0]
