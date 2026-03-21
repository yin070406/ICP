class DLNode:
    def __init__(self, inValue=None, inPrev=None, inNext=None):
        self.value = inValue
        self.prevN = inPrev
        self.nextN = inNext

class DLList:
    def __init__(self):
        self.headN = 0
        self.tailN = 0

    def sizeL(self):
        counter = 0
        curN = self.headN
        while curN != None:
            curN = curN.nextN
            counter += 1
        return counter
    
    def insertL(self, inValue, pos):
        last = self.sizeL()
        if pos < 1 or pos > last+1:
            return None
        elif pos == 1:
            newN = DLNode(inValue, inNext=self.headN)
            curN = self.headN
            self.headN = newN
            curN.prevN = newN
            if self.headN.nextN == 0:
                self.tailN = newN
                self.headN = newN
        else:
            curN = self.headN
            for i in range(0, pos-2):
                curN = curN.nextN
            newN = DLNode(inValue, curN, curN.nextN)
            curN.nextN = newN
            if newN.nextN != None:
                newN.prevN = curN
                curN = newN.nextN
                curN.prevN = newN
            else:
                self.tailN = newN
    
    def reverse(self):
        if self.sizeL() != 1 and self.headN != 0:
            curN = self.headN
            for i in range(0, self.sizeL()):
                origNextN = curN.nextN
                curN.nextN = curN.prevN
                curN.prevN = origNextN
                curN = curN.prevN
            origHeadN = self.headN
            self.headN = self.tailN
            self.tailN = origHeadN

    def appendL(self, elt):
        if self.headN == 0:
            newN = DLNode(elt)
            self.headN = newN
            self.tailN = newN
        else:
            newN = DLNode(elt, self.tailN)
            self.tailN.nextN = newN
            self.tailN = newN