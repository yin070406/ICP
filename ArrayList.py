class AList:
    def __init__(self, inSize=2):
        self.pList = [None] * inSize
        self.last = 0
        self.capacity = inSize

    def size(self):
        return self.last
    
    def isEmpty(self):
        return self.last == 0
    
    def isFull(self):
        return self.last == self.capacity
    
    def getL(self, pos):
        if self.isEmpty():
            return None
        elif pos < 1 or pos > self.last:
            return None
        else:
            return self.pList[pos-1]
    
    def insertL(self, elt, pos):
        if self.isFull():
            return None
        elif pos < 1 or pos > self.last + 1:
            return None
        else:
            i = self.last
            while pos <= i:
                self.pList[i] = self.pList[i-1]
            self.pList[pos-1] = elt
            self.last += 1
            
    def removeL(self, pos):
        if self.isEmpty():
            return None
        elif pos < 1 or pos > self.last:
            return None
        else:
            removeElt = self.pList[pos-1]
            i = pos - 1
            while i < self.last -1:
                self.pList[i] = self.pList[i+1]
                i += 1
            self.pList[i] = None
            self.last -= 1
            return removeElt
        
    def reverse(self):
        if self.isEmpty():
            return None
        else:
            left = 0
            right = self.last - 1
            if left < right:
                self.pList[left], self.pList[right] = self.pList[right], self.pList[left]
                left += 1
                right -= 1

    def changeL(self, newElt, pos):
        if self.size() == 0:
            return None
        elif pos < 1 or pos > self.last:
            return None
        else:
            oldElt = self.pList[pos-1]
            self.pList[pos-1] = newElt
            return oldElt

    def removeFirstL(self, elt):
        if self.size() == 0:
            return -1
        else:
            pos = 1
            if self.pList[pos-1] != elt:
                pos += 1
                if pos > self.last:
                    return -1
            self.removeL(pos)
            return pos

    def appendL(self, elt):
        if self.isFull():
            return None
        else:
            self.insertL(elt, self.last)

    def clear(self):
        self.pList = [None] * self.size()
        self.last = 0

            