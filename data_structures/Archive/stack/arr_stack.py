class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if  not self.is_empty():
           return self.stack.pop()
        return "Stack is Empty"
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
s = ArrayStack()

s.push(10)
s.push(20)
print(s.stack)
s.pop()
print(s.stack)
