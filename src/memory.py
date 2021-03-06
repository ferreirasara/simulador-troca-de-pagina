from random import randint


class Memory:
    """
    Class to simulate memory.
    """
    memory = {
        'length': 0,
        'physicalMemory': []
    }

    def __init__(self, length, initialState):
        """
        Create an object Memory.

        :param length: length of memory.
        :param initialState: list with processes.
        :type length: int
        :type initialState: list[str]
        """
        self.memory['length'] = length
        self.memory['physicalMemory'] = [[process, 1, 1, 1, 0, randint(0, 9999)] for process in initialState]  # [process, valid, present, referenced, modified, frame/disk]

    def reset(self, initialState):
        """
        Reset memory to initial state.

        :param initialState:  list with processes.
        :type initialState: list[str]
        """
        self.memory['physicalMemory'] = [[process, 1, 1, 1, 0, randint(0, 9999)] for process in
                                         initialState]  # [process, valid, present, referenced, modified, frame/disk]

    def getProcessIndex(self, process):
        """
        Search a process, and return index.

        :param process: process to be searched.
        :type process: str
        :return: index of process.
        :rtype: int
        """
        for i in range(self.memory['length']):
            if self.memory['physicalMemory'][i][0] == process:
                return i
        return -1

    def getProcessesAndBits(self):
        """
        Return a list with processes and bits (valid, present, referenced, modified, frame/disk).

        :return: a list with processes and bits.
        :rtype: list[list[str, int, int, int, int, int]]
        """
        return self.memory['physicalMemory']

    def getOnlyProcesses(self):
        """
        Return a list with only processes.

        :return: a list with processes.
        :rtype: list[list[str]]
        """
        return [p[0] for p in self.memory['physicalMemory']]

    def getlength(self):
        """
        Return length of memory.

        :return: length.
        :rtype: int
        """
        return self.memory['length']

    def memoryIsFull(self):
        """
        Verify if memory is full.

        :return: Memory full.
        :rtype: bool
        """
        return '0' not in self.getOnlyProcesses()

    def processValid(self, process):
        """
        Verify valid bit of a process.

        :param process: process to be verified.
        :type process: str
        :return: Process valid.
        :rtype: bool
        """
        for i in range(self.memory['length']):
            if self.memory['physicalMemory'][i][0] == process:
                return self.memory['physicalMemory'][i][1] == 1
        return False

    def processPresent(self, process):
        """
        Verify present bit of a process.

        :param process: process to be verified.
        :type process: str
        :return: Process present.
        :rtype: bool
        """
        for i in range(self.memory['length']):
            if self.memory['physicalMemory'][i][0] == process:
                return self.memory['physicalMemory'][i][2] == 1
        return False

    def processReferenced(self, process):
        """
        Verify referenced bit of a process.

        :param process: process to be verified.
        :type process: str
        :return: Process referenced.
        :rtype: bool
        """
        for i in range(self.memory['length']):
            if self.memory['physicalMemory'][i][0] == process:
                return self.memory['physicalMemory'][i][3] == 1
        return False

    def processModified(self, process):
        """
        Verify modified bit of a process.

        :param process: process to be verified.
        :type process: str
        :return: Process modified.
        :rtype: bool
        """
        for i in range(self.memory['length']):
            if self.memory['physicalMemory'][i][0] == process:
                return self.memory['physicalMemory'][i][4] == 1
        return False

    def setValidBit(self, process, bit):
        """
        Set valid bit of a process.

        :param process: process to be searched.
        :param bit: 0 or 1.
        :type process: str
        :type bit: int
        """
        for i in range(self.memory['length']):
            if self.memory['physicalMemory'][i][0] == process:
                self.memory['physicalMemory'][i][1] = bit

    def setPresentdBit(self, process, bit):
        """
        Set present bit of a process.

        :param process: process to be searched.
        :param bit: 0 or 1.
        :type process: str
        :type bit: int
        """
        for i in range(self.memory['length']):
            if self.memory['physicalMemory'][i][0] == process:
                self.memory['physicalMemory'][i][2] = bit

    def setReferencedBit(self, process, bit):
        """
        Set referenced bit of a process.

        :param process: process to be searched.
        :param bit: 0 or 1.
        :type process: str
        :type bit: int
        """
        for i in range(self.memory['length']):
            if self.memory['physicalMemory'][i][0] == process:
                self.memory['physicalMemory'][i][3] = bit

    def setModifiedBit(self, process, bit):
        """
        Set modified bit of a process.

        :param process: process to be searched.
        :param bit: 0 or 1.
        :type process: str
        :type bit: int
        """
        for i in range(self.memory['length']):
            if self.memory['physicalMemory'][i][0] == process:
                self.memory['physicalMemory'][i][4] = bit

    def appendToMemory(self, process):
        """
        Add an process to memory.

        :param process: process to be added.
        :type process: str
        :return: returns true if the process was added, or false if it was not added.
        :rtype: bool
        """
        if self.memoryIsFull():
            return False
        else:
            for i in range(self.memory['length']):
                if self.memory['physicalMemory'][i][0] == '0':
                    self.memory['physicalMemory'][i][0] = process  # Process
                    self.memory['physicalMemory'][i][1] = 1  # Valid
                    self.memory['physicalMemory'][i][2] = 1  # Present
                    self.memory['physicalMemory'][i][3] = 1  # Referenced
                    self.memory['physicalMemory'][i][4] = 0  # Modified
                    self.memory['physicalMemory'][i][5] = randint(0, 9999)  # Frame/Disk
                    return True

    def removeFromMemory(self, indexProcessToRemove):
        """
        Remove an process to memory.

        :param indexProcessToRemove: index of a process to be removed.
        :type indexProcessToRemove: int
        :return: returns true if the process was removed, or false if it was not removed.
        :rtype: bool
        """
        if self.memory['physicalMemory'][indexProcessToRemove][0]:
            self.memory['physicalMemory'][indexProcessToRemove][0] = '0'  # Process
            self.memory['physicalMemory'][indexProcessToRemove][1] = 0  # Valid
            self.memory['physicalMemory'][indexProcessToRemove][2] = 0  # Present
            self.memory['physicalMemory'][indexProcessToRemove][3] = 0  # Referenced
            self.memory['physicalMemory'][indexProcessToRemove][4] = 0  # Modified
            self.memory['physicalMemory'][indexProcessToRemove][5] = randint(0, 9999)  # Frame/Disk
            return True
        return False

    def replaceProcess(self, indexProcessToReplace, newProcess):
        """
        Replace a process in memory, by other process.

        :param indexProcessToReplace: index of a process to be replaced.
        :param newProcess: process to be added.
        :type indexProcessToReplace: int
        :type newProcess: str
        :return: returns true if the process was replaced, or false if it was not replaced.
        :rtype: bool
        """
        if self.memory['physicalMemory'][indexProcessToReplace][0]:
            self.memory['physicalMemory'][indexProcessToReplace][0] = newProcess  # Process
            self.memory['physicalMemory'][indexProcessToReplace][1] = 1  # Valid
            self.memory['physicalMemory'][indexProcessToReplace][2] = 1  # Present
            self.memory['physicalMemory'][indexProcessToReplace][3] = 1  # Referenced
            self.memory['physicalMemory'][indexProcessToReplace][4] = 0  # Modified
            self.memory['physicalMemory'][indexProcessToReplace][5] = randint(0, 9999)  # Frame/Disk
            return True
        return False

    def __str__(self):
        processes = [p[0] for p in self.memory['physicalMemory']]
        return ' '.join(processes)
