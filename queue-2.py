from collections import deque

class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        if self.queue1:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self):
        if self.queue1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())
            return self.queue1.popleft()
        else:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.popleft())
            return self.queue2.popleft()

    def top(self):
        if self.queue1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())
            top_element = self.queue1[0]
            self.queue2.append(self.queue1.popleft())
            return top_element
        else:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.popleft())
            top_element = self.queue2[0]
            self.queue1.append(self.queue2.popleft())
            return top_element

    def empty(self):
        return not self.queue1 and not self.queue2

myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())  
print(myStack.pop())  
print(myStack.empty())  
