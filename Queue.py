class Queue():
    def __init__(self, inSize=6):
        self.pList = [None] * inSize
        self.head = 0
        self.tail = 0
        self.capacity = inSize

    def size(self):
        return self.tail - self.head
    
    def isEmpty(self):
        return self.head == 0
    
    def enqueue(self, elt):
        newCapacity *= 2
        newPList = [None] * newCapacity
        for i in range(0, self.size()):
            newPList[i] = self.pList[i]
        self.pList = newPList
        self.pList[self.tail+1] = elt
        self.tail += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            removeElt = self.pList[self.head]
            self.pList[self.head] = None
            self.head += 1
            if self.size() == 0:
                self.head = 0
                self.tail = self.head
            return removeElt
        
    def reverse(self):
        if self.isEmpty():
            return None
        else:
            values = []
            while not self.isEmpty():
                values.append(self.dequeue)
            for i in range(0, self.size()-1, -1, -1):
                self.enqueue(values[i])