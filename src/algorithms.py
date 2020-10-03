from util import calcLRUMatrixValue, getMinorValueLRUMatrix, setValueInLRUMatrix

def optimalAlgorithm(memory, processQueue):
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


def fifo(memory, processQueue):
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


def secondChance(memory, processQueue):
    print('Physical Memory (Initial): ', memory)
    numberOfFaults = 0
    fifoQueue = memory.getOnlyProcesses()
    for process in processQueue:
        processesInMemory = memory.getOnlyProcesses()
        if process != '|':  # Ignore clock
            if process not in processesInMemory:  # If actual process not in memory, cause a segmentation fault
                print('Segmentation Fault on process ', process)
                print(fifoQueue)
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


def lru(memory, processQueue):
    print('Physical Memory (Initial): ', memory)
    numberOfFaults = 0
    matrix = [[0 for i in range(memory.getLenght() + 1)] for n in range(memory.getLenght())]
    # TODO calcular historico
    calcLRUMatrixValue(matrix)
    for process in processQueue:
        processesInMemory = memory.getOnlyProcesses()
        if process != '|':  # Ignore clock
            if process not in processesInMemory:  # If actual process not in memory, cause a segmentation fault
                print('Segmentation Fault on process ', process)
                if not memory.appendToMemory(process):  # If memory is full
                    processToRemove = processesInMemory[getMinorValueLRUMatrix(matrix)]
                    memory.replaceProcess(processToRemove, process)  # Replaces with first process in queue
                    print('Replaced process ', processToRemove[0], ' by process ', process)
                    numberOfFaults += 1
            processesInMemory = memory.getOnlyProcesses()
            setValueInLRUMatrix(matrix, processesInMemory.index(process))
            calcLRUMatrixValue(matrix)
        print('Physical Memory: ', memory)

    print('\nLRU Algorithm finalized. Number of faults: ', numberOfFaults, '\n')
