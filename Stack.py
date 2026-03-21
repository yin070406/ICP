class Stack:
    def __init__(self, inSize=6):
        self.pList = [None] * inSize
        self.top = 0
        self.capacity = inSize

    def size(self):
        return self.top+1
    
    def isEmpty(self):
        return self.top == 0

    def push(self, elt):
        newCapacity *= 2
        newPList = [None] * newCapacity
        for i in range(0, self.size()):
            newPList[i] = self.pList[i]
        self.pList = newPList
        self.top += 1
        self.pList[self.top] = elt

    def pop(self):
        if self.isEmpty(self):
            return None
        else:
            removeElt = self.pList[self.top]
            self.pList[self.top] = None
            self.top -= 1
            return removeElt
        
    def reverse(self):
        if self.isEmpty():
            return None
        else:
            temp1 = Stack(self.capacity)
            temp2 = Stack(self.capacity)
            while not self.isEmpty():
                temp1.push(self.pop())
            while not temp1.isEmpty():
                temp2.push(temp1.pop())
            while not temp2.isEmpty():
                self.push(temp2.pop())