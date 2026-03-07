class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
class Hash_Table:
    """
    The default capacity is 11 elements.
    """
    def __init__(self, capacity:int = 11):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key) -> int:
        hash_value = 0
        prime_multiplier = 31

        for char in str(key):
            # # ord(char) -> returns the ASCII number of 'char'
            hash_value = (hash_value * prime_multiplier) + ord(char)
        
        return hash_value % self.capacity
    
    def _resize(self) -> None:
        old_table = self.table
        self.capacity = self.capacity * 2 + 1
        self.table = [None] * self.capacity
        self.size = 0
        
        for node in old_table:
            current = node
            while current:
                self.insert(current.key, current.value)
                current = current.next
    
    def insert(self, key, value) -> None:
        if self.size / self.capacity > 0.7:
            self._resize()
        
        index = self._hash(key)
        
        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return 
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1
        
    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)
    
    def remove(self, key):
        index = self._hash(key)
        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next
        raise KeyError(key)
    
    def clear(self):
        self.table = [None] * self.capacity
        self.size = 0
        self.capacity = 11

    def keys(self) -> list:
        all_keys = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                all_keys.append(current.key)
                current = current.next
        return all_keys
    
    def values(self) -> list:
        all_values = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                all_values.append(current.value)
                current = current.next
        return all_values
    
    def get_stats(self) -> None:
        lengths = []
        for i in range(self.capacity):
            count = 0
            current = self.table[i]
            while current:
                count += 1
                current = current.next
            lengths.append(count)
        max_len = max(lengths) if lengths else 0
        non_empty_buckets = len([l for l in lengths if l > 0])

        print("Hash Tabls Stats")
        print(f"Capacity: {self.capacity}")
        print(f"Size: {self.size}")
        print(f"Non-empty Buckets: {non_empty_buckets}")
        print(f"Max-Chain Length: {max_len}")
        print(f"Average Chain Length: {self.size / non_empty_buckets if non_empty_buckets else 0:.2f}")

    def __str__(self, limit=20) -> str:
        res_list = [f"Hash Table Summary: Size={self.size}, Capacity={self.capacity}"]
        count = 0

        for i in range(self.capacity):
            if self.table[i] is not None:
                current = self.table[i]
                nodes = []
                while current:
                    nodes.append(f"[{current.key}: {current.value}]")
                    current = current.next
                
                res_list.append(f"Bucket {i}: {' -> '.join(nodes)}")
                count += 1
            if count >= limit:
                res_list.append(f"... and many more filled buckets.")
                break
        if count == 0:
            res_list.append("The table is empty")
        
        return "\n".join(res_list)
    
    def __repr__(self):
        items = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                items.append(f"{repr(current.key)}:{repr(current.value)}")
                current = current.next
        return "{" + ", ".join(items) + "}"
    
    def __len__(self):
        return self.size

    def __contains__(self, item):
        try:
            self.search(item)
            return True
        except KeyError:
            return False
    
    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.search(key)
