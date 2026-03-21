class Node:
    def __init__(self, inValue=None, inNext=None):
        self.value = inValue
        self.nextN = inNext

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, inValue):
        newN = Node(inValue, None)
        if self.head == None:
            self.head = newN
            self.tail = newN
        else:
            self.tail.nextN = newN
            self.tail = newN

    def dequeue(self):
        if self.head == None:
            return None
        else:
            origHeadN = self.head
            self.head = origHeadN.nextN
            origHeadN.nextN = None
            if self.head == None:
                self.tail = None

    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head.value
        
    def reverse(self):
        tempQ = Queue()
        values = []
        curN = self.head
        while curN != None:
            values.append(curN.value)
            curN = curN.nextN
        for i in reversed(values):
            tempQ.enqueue(values[i])
        return tempQ