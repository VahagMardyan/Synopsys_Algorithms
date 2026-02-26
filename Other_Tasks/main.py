from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
    @abstractmethod
    def get_value(self) -> bool:
        pass

class Leaf(Node):
    def __init__(self, val : bool):
        super().__init__()
        self.value = val
    def get_value(self) -> bool:
        return self.value
    
class And_Node(Node):
    def get_value(self) -> bool:
        return self.left.get_value() and self.right.get_value()
    
class Or_Node(Node):
    def get_value(self) -> bool:
        return self.left.get_value() or self.right.get_value()

def evaluate(node : Node) -> bool:
    return node.get_value()

e4 = And_Node()
e4.left, e4.right = Leaf(True), Leaf(False)

e2 = Or_Node()
e2.left, e2.right = e4, Leaf(True)

e5 = Or_Node()
e5.left, e5.right = Leaf(False), Leaf(False)

e6 = Or_Node()
e6.left, e6.right = Leaf(True), Leaf(False)

e3 = And_Node()
e3.left, e3.right = e5, e6

e1 = And_Node()
e1.left, e1.right = e2, e3

print(f"Result is: {evaluate(e1)}") # # False