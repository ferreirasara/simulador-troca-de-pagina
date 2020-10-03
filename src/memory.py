from random import randint


class Memory:
    memory = {
        'lenght': 0,
        'physicalMemory': []
    }

    def __init__(self, lenght, initialState):
        self.memory['lenght'] = lenght
        self.memory['physicalMemory'] = [[process, 1, 1, 1, 0, randint(0, 9999)] for process in initialState]  # [process, valid, present, referenced, modified, frame/disk]

    def getProcessIndex(self, process):
        for i in range(self.memory['lenght']):
            if self.memory['physicalMemory'][i][0] == process:
                return i
        return -1

    def getProcessesAndBits(self):
        return self.memory['physicalMemory']

    def getOnlyProcesses(self):
        return [p[0] for p in self.memory['physicalMemory']]

    def getLenght(self):
        return self.memory['lenght']

    def memoryIsFull(self):
        return '0' not in self.getOnlyProcesses()

    def processValid(self, process):
        for i in range(self.memory['lenght']):
            if self.memory['physicalMemory'][i][0] == process:
                return self.memory['physicalMemory'][i][1] == 1
        return False

    def processPresent(self, process):
        for i in range(self.memory['lenght']):
            if self.memory['physicalMemory'][i][0] == process:
                return self.memory['physicalMemory'][i][2] == 1
        return False

    def processReferenced(self, process):
        for i in range(self.memory['lenght']):
            if self.memory['physicalMemory'][i][0] == process:
                return self.memory['physicalMemory'][i][3] == 1
        return False

    def processModified(self, process):
        for i in range(self.memory['lenght']):
            if self.memory['physicalMemory'][i][0] == process:
                return self.memory['physicalMemory'][i][4] == 1
        return False

    def setValidBit(self, process, bit):
        for i in range(self.memory['lenght']):
            if self.memory['physicalMemory'][i][0] == process:
                self.memory['physicalMemory'][i][1] = bit

    def setPresentdBit(self, process, bit):
        for i in range(self.memory['lenght']):
            if self.memory['physicalMemory'][i][0] == process:
                self.memory['physicalMemory'][i][2] = bit

    def setReferencedBit(self, process, bit):
        for i in range(self.memory['lenght']):
            if self.memory['physicalMemory'][i][0] == process:
                self.memory['physicalMemory'][i][3] = bit

    def setModifiedBit(self, process, bit):
        for i in range(self.memory['lenght']):
            if self.memory['physicalMemory'][i][0] == process:
                self.memory['physicalMemory'][i][4] = bit

    def appendToMemory(self, process):
        if self.memoryIsFull():
            return False
        else:
            for i in range(self.memory['lenght']):
                if self.memory['physicalMemory'][i][0] == '0':
                    self.memory['physicalMemory'][i][0] = process # Process
                    self.memory['physicalMemory'][i][1] = 1  # Valid
                    self.memory['physicalMemory'][i][2] = 1  # Present
                    self.memory['physicalMemory'][i][3] = 1  # Referenced
                    self.memory['physicalMemory'][i][4] = 0  # Modified
                    self.memory['physicalMemory'][i][5] = randint(0, 9999)  # Frame/Disk
                    return True

    def removeFromMemory(self, process):
        for i in range(self.memory['lenght']):
            if self.memory['physicalMemory'][i][0] == process:
                self.memory['physicalMemory'][i][0] = '0'  # Process
                self.memory['physicalMemory'][i][1] = 0  # Valid
                self.memory['physicalMemory'][i][2] = 0  # Present
                self.memory['physicalMemory'][i][3] = 0  # Referenced
                self.memory['physicalMemory'][i][4] = 0  # Modified
                self.memory['physicalMemory'][i][5] = randint(0, 9999)  # Frame/Disk
                return True
        return False

    def replaceProcess(self, processToReplace, newProcess):
        for i in range(self.memory['lenght']):
            if self.memory['physicalMemory'][i][0] == processToReplace:
                self.memory['physicalMemory'][i][0] = newProcess  # Process
                self.memory['physicalMemory'][i][1] = 1  # Valid
                self.memory['physicalMemory'][i][2] = 1  # Present
                self.memory['physicalMemory'][i][3] = 1  # Referenced
                self.memory['physicalMemory'][i][4] = 0  # Modified
                self.memory['physicalMemory'][i][5] = randint(0, 9999)  # Frame/Disk
                return True
        return False

    def __str__(self):
        processes = [p[0] for p in self.memory['physicalMemory']]
        return ' '.join(processes)
