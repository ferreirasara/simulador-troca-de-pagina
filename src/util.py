def getSettings(file):
    """
    This functions receives a file, process and validate information, and finally return a list with configurations to simulator.

    :param file: a file open previously.
    :type file: TextWrapper
    :return: list with configurations
    :rtype: tuple[int, list[str], list[str], list[str]]
    """
    lines = [line.strip() for line in file]
    if len(lines) < 4:
        print('ERROR - Invalid number of lines.')
        return None

    length = lines[0]
    initialState = lines[1].split(',')
    processQueue = lines[2].split(',')
    processAction = lines[3].split(',')

    if length.isdigit():
        length = int(length)
        if length > 0:
            if len(initialState) == length:
                if len(processQueue) == len(processAction):
                    if '0' not in processQueue:
                        return length, initialState, processQueue, processAction
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
