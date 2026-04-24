class PriorityNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None
    
    def enqueue(self, data, priority):
        new_node = PriorityNode(data, priority)
        if not self.front or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
    
    def dequeue(self):
        if not self.front:
            return "Empty"
        data = self.front.data
        self.front = self.front.next
        return data
    
    def print_queue(self):
        if not self.front:
            print("Priority Queue is Empty")
            return
        this_node = self.front
        print("--- Priority Order ---")
        while this_node:
            print(f"Data: {this_node.data} (P: {this_node.priority})")
            this_node = this_node.next
        print("-----------------------")

priority_q = PriorityQueue()
priority_q.enqueue("Message",3) # Low priority
priority_q.enqueue("ALERT",1) # High priority
priority_q.enqueue("Payment",2) # Medium priority

priority_q.print_queue()

