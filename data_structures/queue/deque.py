class DequeNode:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

class Deque:
    def __init__(self):
        self.front = self.rear = None

    def add_rear(self, data):
        new_node = DequeNode(data)

        if not self.rear:
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def add_front(self, data):
        new_node = DequeNode(data)
        if not self.front:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def remove_front(self):
        if not self.front:
            return "Empty"
        data = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        return data
    
    def print_deque(self):
        if not self.front:
            print("Deque is Empty")
            return
        
        this_node = self.front
        result = "Front <-> "
        while this_node:
            result += f"[{this_node.data}] <-> "
            this_node = this_node.next
        print(result + "Rear")

dq = Deque()
dq.add_rear("Middle")
dq.add_front("Start")
dq.add_rear("End")
dq.print_deque()