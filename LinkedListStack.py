class Node:
    def __init__(self, inValue, inNext=None):
        self.value = inValue
        self.nextN = inNext

class Stack:
    def __init__(self):
        self.headN = 0
        self.count = 0

    def push(self, inValue):
        newN = Node(inValue, self.headN)
        self.headN = newN
        self.count += 1

    def pop(self):
        if self.headN == None:
            return None
        else:
            origHead = self.headN
            self.headN = origHead.nextN
            origHead.nextN = None
            self.count -= 1
            return origHead
    
    def peek(self):
        if self.headN == 0:
            return None
        else:
            return self.headN.value
        
    def isEmpty(self):
        return self.headN == 0
    
    def sizeL(self):
        return self.count
    
    def reverse(self):
        prevN = None
        curN = self.headN
        while curN != 0:
            next_node = curN.nextN
            curN.nextN = prevN
            prevN = curN
            curN = next_node
        self.headN = prevN
