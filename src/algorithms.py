import util


def optimalAlgorithm(memory, processQueue):
    """
    This algorithm is the best way to manage memory. But is impossible to implement in real life, because there is no
    way to know what process will be in next.

    :param memory: memory obj, create previously.
    :param processQueue: list with processes to be executed.
    :return: return number of faults.
    :rtype: int
    :type memory: memory.Memory
    :type processQueue: list
    """

    print('Physical Memory (Initial): ', memory)
    numberOfFaults = 0
    for i in range(len(processQueue)):
        processesInMemory = memory.getOnlyProcesses()
        if processQueue[i] != '|':  # Ignore clock
            if processQueue[i] not in processesInMemory:  # If actual process not in memory, cause a segmentation fault
                print('Segmentation Fault on process ', processQueue[i])
                if not memory.appendToMemory(processQueue[i]):  # If memory is full
                    processToRemove = ['', 0]
                    for processInMemory in processesInMemory:  # Counts how long it will take for the process to be requested again
                        count = 0
                        for p in processQueue[i:]:  # Considers the queue from the current position
                            if p != processInMemory:
                                count += 1
                            else:
                                break
                        if count > processToRemove[1]:
                            processToRemove[0] = processInMemory
                            processToRemove[1] = count
                    memory.replaceProcess(processToRemove[0], processQueue[i])  # Replaces with the process that will take longer to be requested
                    print('Replaced process ', processToRemove[0], ' by process ', processQueue[i])
                    numberOfFaults += 1
        print('Physical Memory: ', memory)
    print('\nOptimal Algorithm finalized. Number of faults: ', numberOfFaults, '\n')
    return numberOfFaults


def fifo(memory, processQueue):
    """
    This algorithm implements a simple fifo queue to decide which process will be replaced.

    :param memory: memory obj, create previously.
    :param processQueue: list with processes to be executed.
    :return: return number of faults.
    :rtype: int
    :type memory: memory.Memory
    :type processQueue: list
    """

    print('Physical Memory (Initial): ', memory)
    numberOfFaults = 0
    fifoQueue = memory.getOnlyProcesses()
    for process in processQueue:
        processesInMemory = memory.getOnlyProcesses()
        if process != '|':  # Ignore clock
            if process not in processesInMemory:  # If actual process not in memory, cause a segmentation fault
                print('Segmentation Fault on process ', process)
                if not memory.appendToMemory(process):  # If memory is full
                    processToRemove = fifoQueue.pop(0)
                    memory.replaceProcess(processToRemove, process)  # Replaces with first process in queue
                    fifoQueue.append(process)  # Add new process to end of queue
                    print('Replaced process ', processToRemove[0], ' by process ', process)
                    numberOfFaults += 1
                else:
                    for i in range(len(fifoQueue)):
                        if fifoQueue[i] == '0':
                            fifoQueue[i] = process
                            break
        print('Physical Memory: ', memory)

    print('\nFifo Algorithm finalized. Number of faults: ', numberOfFaults, '\n')
    return numberOfFaults


def secondChance(memory, processQueue):
    """
    This algorithm implements a simple fifo queue to decide which process will be replaced. But, instead of get the
    first process in queue, the algorithm verify the referenced bit.

    :param memory: memory obj, create previously.
    :param processQueue: list with processes to be executed.
    :return: return number of faults.
    :rtype: int
    :type memory: memory.Memory
    :type processQueue: list
    """

    print('Physical Memory (Initial): ', memory)
    numberOfFaults = 0
    fifoQueue = memory.getOnlyProcesses()
    for process in processQueue:
        processesInMemory = memory.getOnlyProcesses()
        if process != '|':  # Ignore clock
            if process not in processesInMemory:  # If actual process not in memory, cause a segmentation fault
                print('Segmentation Fault on process ', process)
                if not memory.appendToMemory(process):  # If memory is full
                    while memory.processReferenced(fifoQueue[0]):  # While referenced bit is 1, set referenced bit to 0 and move process to end of queue
                        memory.setReferencedBit(fifoQueue[0], 0)
                        p = fifoQueue.pop(0)
                        fifoQueue.append(p)

                    processToRemove = fifoQueue.pop(0)  # Now, referenced bit is 0
                    memory.replaceProcess(processToRemove, process)
                    fifoQueue.append(process)
                    print('Replaced process ', processToRemove[0], ' by process ', process)
                    numberOfFaults += 1
                else:
                    for i in range(len(fifoQueue)):
                        if fifoQueue[i] == '0':
                            fifoQueue[i] = process
                            break
            memory.setReferencedBit(process, 1)  # Set referenced bit to 1, process in use
        else:
            for processInMemory in processesInMemory:
                memory.setReferencedBit(processInMemory, 0)  # Set referenced bit to 0 on clock
        print('Physical Memory: ', memory)

    print('\nSecond Chance Algorithm finalized. Number of faults: ', numberOfFaults, '\n')
    return numberOfFaults


def lru(memory, processQueue):
    """
    This algorithm implements a matrix to calculate which process has been unused for the longest time.

    :param memory: memory obj, create previously.
    :param processQueue: list with processes to be executed.
    :return: return number of faults.
    :rtype: int
    :type memory: memory.Memory
    :type processQueue: list
    """

    print('Physical Memory (Initial): ', memory)
    numberOfFaults = 0
    matrix = [[0 for i in range(memory.getLenght() + 1)] for n in range(memory.getLenght())]
    processesInMemory = memory.getOnlyProcesses()
    for i in range(len(processesInMemory)):
        if processesInMemory[i] != 0:
            util.setValueInLRUMatrix(matrix, i)
            util.calcLRUMatrixValue(matrix)
    util.calcLRUMatrixValue(matrix)
    for process in processQueue:
        processesInMemory = memory.getOnlyProcesses()
        if process != '|':  # Ignore clock
            if process not in processesInMemory:  # If actual process not in memory, cause a segmentation fault
                print('Segmentation Fault on process ', process)
                if not memory.appendToMemory(process):  # If memory is full
                    processToRemove = processesInMemory[util.getMinorValueLRUMatrix(matrix)]
                    memory.replaceProcess(processToRemove, process)  # Replaces with first process in queue
                    print('Replaced process ', processToRemove[0], ' by process ', process)
                    numberOfFaults += 1
            processesInMemory = memory.getOnlyProcesses()
            util.setValueInLRUMatrix(matrix, processesInMemory.index(process))
            util.calcLRUMatrixValue(matrix)
        print('Physical Memory: ', memory)

    print('\nLRU Algorithm finalized. Number of faults: ', numberOfFaults, '\n')
    return numberOfFaults


def nru(memory, processQueue, actionQueue):
    """
    This algorithm implements a matrix to calculate which process has been unused for the longest time.

    :param memory: memory obj, create previously.
    :param processQueue: list with processes to be executed.
    :param actionQueue: list with action for witch process.
    :return: return number of faults.
    :rtype: int
    :type memory: memory.Memory
    :type processQueue: list
    :type actionQueue: list
    """
    print('Physical Memory (Initial): ', memory)
    numberOfFaults = 0
    for i in range(len(processQueue)):
        processesClass = [[process[0], process[3], process[4], 0] for process in memory.getProcessesAndBits()]
        util.calcClassOfNRUProcesses(processesClass)
        processesInMemory = memory.getOnlyProcesses()
        if processQueue[i] != '|':  # Ignore clock
            if processQueue[i] not in processesInMemory:  # If actual process not in memory, cause a segmentation fault
                print('Segmentation Fault on process ', processQueue[i])
                if not memory.appendToMemory(processQueue[i]):  # If memory is full
                    # TODO remover o processo com classe mais baixa
                    processToRemove = processesInMemory[util.getMinorClassNRU(processesClass)]
                    memory.replaceProcess(processToRemove, processQueue[i])
                    print('Replaced process ', processToRemove, ' by process ', processQueue[i])
                    numberOfFaults += 1
                    if actionQueue[i] == 'W':
                        memory.setModifiedBit(processQueue[i], 1)
                    else:
                        memory.setModifiedBit(processQueue[i], 0)
            memory.setReferencedBit(processQueue[i], 1)
        else:
            for processInMemory in processesInMemory:
                memory.setReferencedBit(processInMemory, 0)
        print('Physical Memory: ', memory)

    print('\nNRU Algorithm finalized. Number of faults: ', numberOfFaults, '\n')
    return numberOfFaults
