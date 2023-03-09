class Deque:
    def __init__(self):
        self.deque = []

    def isEmpty(self):
        return True if self.deque == [] else False
    
    def seeStart(self):
        return self.deque[len(self.deque)-1]
    
    def seeLast(self):
        return self.deque[0]
    
    def insertStart(self,elemento):
        self.deque.append(elemento)

    def insertLast(self,elemento):
        self.deque.insert(0,elemento)
    
    def removeStart(self):
        return self.deque.pop()
    
    def removeLast(self):
        return self.deque.pop(0)
    
    def size(self):
        return len(self.deque)
