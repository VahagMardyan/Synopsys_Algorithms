class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.size = 0
        self.rear = capacity - 1
    
    def enqueue(self, item):
        if self.size == self.capacity:
            print("Queue is Full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            return "Queue is Empty"
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def print_queue(self):
        if self.size == 0:
            print("Queue is Empty")
            return
        print("Front ->", end=" ")
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            print(f"[{self.queue[index]}]", end=" ")
        print("<- Rear")

arr_q = ArrayQueue(5) # # capacity is 5
arr_q.enqueue("A")
arr_q.enqueue("B")
arr_q.enqueue("C")
# print(arr_q.dequeue()) # # A
arr_q.enqueue("D")
arr_q.enqueue(5)
arr_q.enqueue(563) # # Queue is full
arr_q.print_queue() # # 