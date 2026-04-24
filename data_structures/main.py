class ArrayStack:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def is_empty(self):
        return self.top == -1
    
    def push(self,x):
        self.top += 1
        if self.top == len(self.stack):
            self.stack.append(x)
        else:
            self.stack[self.top] = x
        print(f"PUSH({x}) -> stack: {self.stack[:self.top + 1]}")

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        x = self.stack[self.top]
        self.top -= 1
        print(f"POP() → {x}  (stack: {self.stack[:self.top+1]})")
        return x

# # FIFO -> First In First Out

class ArrayQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def enqueue(self, x):
        if self.is_full():
            raise IndexError("Queue overflow")
        
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        print(f"ENQUEUE({x}) -> queue: {self.queue}")

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        x = self.queue[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        print(f"DEQUEUE({x}) -> {x}")
        return x

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.head = None
    
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        print(f"PUSH({x})")
    
    def pop(self):
        if not self.head:
            raise IndexError("Stack underflow")
        
        x = self.head.data
        self.head = self.head.next
        print(f"POP() -> {x}")
        return x
    
class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        print(f"ENQUEUE({x})")

    def dequeue(self):
        if not self.head:
            raise IndexError("Queue underflow")
        
        x = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        print(f"DEQUEUE() -> {x}")
        return x
    
class Deque:
    """O(1)"""
    def __init__(self):
        self.deque = []

    def append(self, x):
        self.deque.append(x)
    
    def pop(self):
        if not self.deque:
            raise IndexError("Deque underflow")
        return self.deque.pop()
    
    def appendLeft(self, x):
        self.deque.insert(0, x)
    
    def popLeft(self):
        if not self.deque:
            raise IndexError("Deque underflow")
        return self.pop(0)
    
    def is_empty(self):
        return len(self.deque) == 0
    
class UndoRedoSystem:
    def __init__(self):
        self.undo_stack = ArrayStack()
        self.redo_stack = ArrayStack()
        self.current_state = None
    
    def do_action(self, new_state):
        if self.current_state is not None:
            self.undo_stack.push(self.current_state)
        self.current_state = new_state
        self.redo_stack = ArrayStack()
        print(f"Action performed → current: {self.current_state}")
    
    def undo(self):
        if self.undo_stack.is_empty():
            print("Nothing to undo")
            return
        self.redo_stack.push(self.current_state)
        self.current_state = self.undo_stack.pop()
        print(f"UNDO → current: {self.current_state}")
    
    def redo(self):
        if self.redo_stack.is_empty():
            print("Nothing to redo")
            return
        self.undo_stack.push(self.current_state)
        self.current_state = self.redo_stack.pop()
        print(f"REDO → current: {self.current_state}")

editor = UndoRedoSystem()
editor.do_action("Text1")
editor.do_action("Text2")
editor.do_action("Text3")
editor.undo()
editor.undo()
editor.redo()
editor.redo()