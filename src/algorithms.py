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
    numberOfFaults = 0
    occurrences = {i: processQueue.count(i) for i in processQueue if i != '|'}
    for i in range(len(processQueue)):
        processesInMemory = memory.getOnlyProcesses()
        if processQueue[i] != '|':  # Ignore clock
            occurrences[processQueue[i]] = occurrences[processQueue[i]]-1
            if occurrences[processQueue[i]] == 0:
                del(occurrences[processQueue[i]])
            if processQueue[i] not in processesInMemory and not memory.appendToMemory(processQueue[i]):  # If actual process not in memory, cause a Page fault and if memory is full
                processToRemove = processesInMemory[-1]
                count = 0
                for process in occurrences:  # Counts how long it will take for the process to be requested again
                    if occurrences[process] > count and process in processesInMemory:
                        processToRemove = process
                        count = occurrences[process]
                memory.replaceProcess(processesInMemory.index(processToRemove), processQueue[i])  # Replaces with the process that will take longer to be requested
                numberOfFaults += 1
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
    numberOfFaults = 0
    fifoQueue = memory.getOnlyProcesses()
    for process in processQueue:
        processesInMemory = memory.getOnlyProcesses()
        if process != '|':  # Ignore clock
            if process not in processesInMemory:  # If actual process not in memory, cause a Page  fault
                if not memory.appendToMemory(process):  # If memory is full
                    processToRemove = fifoQueue.pop(0)
                    memory.replaceProcess(processesInMemory.index(processToRemove), process)  # Replaces with first process in queue
                    fifoQueue.append(process)  # Add new process to end of queue
                    numberOfFaults += 1
                else:
                    for i in range(len(fifoQueue)):
                        if fifoQueue[i] == '0':
                            fifoQueue[i] = process
                            break
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
    numberOfFaults = 0
    fifoQueue = memory.getOnlyProcesses()
    for process in processQueue:
        processesInMemory = memory.getOnlyProcesses()
        if process != '|':  # Ignore clock
            if process not in processesInMemory:  # If actual process not in memory, cause a Page  fault
                if not memory.appendToMemory(process):  # If memory is full
                    while memory.processReferenced(fifoQueue[0]):  # While referenced bit is 1, set referenced bit to 0 and move process to end of queue
                        memory.setReferencedBit(fifoQueue[0], 0)
                        p = fifoQueue.pop(0)
                        fifoQueue.append(p)

                    processToRemove = fifoQueue.pop(0)  # Now, referenced bit is 0
                    memory.replaceProcess(processesInMemory.index(processToRemove), process)
                    fifoQueue.append(process)
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
    numberOfFaults = 0
    matrix = [[0 for i in range(memory.getlength() + 1)] for n in range(memory.getlength())]
    processesInMemory = memory.getOnlyProcesses()
    for i in range(len(processesInMemory)):
        if processesInMemory[i] != 0:
            util.setValueInLRUMatrix(matrix, i)
            util.calcLRUMatrixValue(matrix)
    util.calcLRUMatrixValue(matrix)
    for process in processQueue:
        processesInMemory = memory.getOnlyProcesses()
        if process != '|':  # Ignore clock
            if process not in processesInMemory:  # If actual process not in memory, cause a Page  fault
                if not memory.appendToMemory(process):  # If memory is full
                    processToRemove = processesInMemory[util.getMinorValueLRUMatrix(matrix)]
                    memory.replaceProcess(processesInMemory.index(processToRemove), process)  # Replaces with first process in queue
                    numberOfFaults += 1
            processesInMemory = memory.getOnlyProcesses()
            util.setValueInLRUMatrix(matrix, processesInMemory.index(process))
            util.calcLRUMatrixValue(matrix)
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
    numberOfFaults = 0
    for i in range(len(processQueue)):
        processesClass = [[process[0], process[3], process[4], 0] for process in memory.getProcessesAndBits()]
        util.calcClassOfNRUProcesses(processesClass)
        processesInMemory = memory.getOnlyProcesses()
        if processQueue[i] != '|':  # Ignore clock
            if processQueue[i] not in processesInMemory:  # If actual process not in memory, cause a Page  fault
                if not memory.appendToMemory(processQueue[i]):  # If memory is full
                    processToRemove = processesInMemory[util.getMinorClassNRU(processesClass)]
                    memory.replaceProcess(processesInMemory.index(processToRemove), processQueue[i])
                    numberOfFaults += 1
                    if actionQueue[i] == 'W':
                        memory.setModifiedBit(processQueue[i], 1)
                    else:
                        memory.setModifiedBit(processQueue[i], 0)
            memory.setReferencedBit(processQueue[i], 1)
        else:
            for processInMemory in processesInMemory:
                memory.setReferencedBit(processInMemory, 0)
    return numberOfFaults
