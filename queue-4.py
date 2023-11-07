class MyCircularDeque:
    def __init__(self, k):
        self.size = k
        self.data = [0] * k
        self.front = 0
        self.rear = -1
        self.count = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.size
        self.data[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.data[self.rear] = value
        self.count += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.size
        self.count -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.data[self.rear]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

myCircularDeque = MyCircularDeque(3)
print(myCircularDeque.insertLast(1))  
print(myCircularDeque.insertLast(2))  
print(myCircularDeque.insertFront(3))  
print(myCircularDeque.insertFront(4))  
print(myCircularDeque.getRear())  
print(myCircularDeque.isFull())  
print(myCircularDeque.deleteLast())  
print(myCircularDeque.insertFront(4))  
print(myCircularDeque.getFront())  
