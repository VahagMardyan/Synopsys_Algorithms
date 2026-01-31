class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.front is None:
            return "Queue is Empty"
        
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data
    
    def print_queue(self):
        if not self.front:
            print("Queue is Empty")
            return
        
        this_node = self.front
        result = "Front -> "
        while this_node:
            result += f"[{this_node.data}] "
            this_node = this_node.next
        print(result + "<- Rear")

list_q = ListQueue()
list_q.enqueue("John")
list_q.enqueue("James")
list_q.enqueue("Jane")
print(list_q.dequeue()) # # John
list_q.print_queue()