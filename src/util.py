def getSettings(file):
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
    for i in range(len(matrix)):
        matrix[index][i] = 1

    for i in range(len(matrix)):
        matrix[i][index] = 0


def getMinorValueLRUMatrix(matrix):
    minorValue = [0, 999999]
    for i in range(len(matrix)):
        if matrix[i][-1] <= minorValue[1]:
            minorValue[0] = i
            minorValue[1] = matrix[i][-1]
    return minorValue[0]


def calcLRUMatrixValue(matrix):
    for line in matrix:
        binary = ''.join([str(n) for n in line[:-1]])
        line[-1] = int(binary, 2)
