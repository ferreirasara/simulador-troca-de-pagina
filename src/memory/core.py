class Memory:
    memory = {
        'lenght': 0,
        'physicalMemory': []
    }

    def __init__(self, lenght, initialState):
        self.memory['lenght'] = lenght
        self.memory['physicalMemory'] = initialState

    def memoryIsFull(self):
        return '0' not in self.memory['physicalMemory']

    def appendToMemory(self, process):
        if self.memoryIsFull():
            return False
        else:
            for i in range(self.memory['lenght']):
                if self.memory['physicalMemory'][i] == '0':
                    self.memory['physicalMemory'][i] = process
                    break
            return True

    def removeFromMemory(self, process):
        for i in range(self.memory['lenght']):
            if self.memory['physicalMemory'][i] == process:
                self.memory['physicalMemory'][i] = '0'
                return True
        return False

    def replaceProcess(self, processToReplace, newProcess):
        for i in range(self.memory['lenght']):
            if self.memory['physicalMemory'][i] == processToReplace:
                self.memory['physicalMemory'][i] = newProcess
                return True
        return False

    def __str__(self):
        return self.memory['physicalMemory']
