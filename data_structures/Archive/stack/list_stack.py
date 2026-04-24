class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class ListStack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def print_stack(self):
        if self.is_empty():
            print("Stack is Empty")
            return
        this_node = self.top
        print("--- TOP ---")
        while this_node:
            print(f"|   {this_node.data}   |")
            this_node = this_node.next
        print("-----------")

my_stack = ListStack()
my_stack.push(5)
my_stack.push(45)
my_stack.push(165)

my_stack.print_stack()
my_stack.print_stack()