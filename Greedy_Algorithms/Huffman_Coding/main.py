import heapq

# # Huffman Coding

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
def build_huffman_tree(frequencies):
    # # Priority queue for each character
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    return heap[0] # root

def huffman_encode(node, current_code = "", codes = {}):
    if node is None:
        return
    
    if node.char is not None:
        codes[node.char] = current_code
    
    huffman_encode(node.left, current_code + "0", codes)
    huffman_encode(node.right, current_code + "1", codes)

    return codes

def huffman_decode(root, encoded_str):
    decoded_output = ""
    current_node = root

    for bit in encoded_str:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.left is None and current_node.right is None:
            decoded_output += current_node.char
            current_node = root

    return decoded_output

freq_map = {'A': 45, 'B': 13, 'C': 12, 'D': 16, 'E': 9, 'F': 5}
root = build_huffman_tree(freq_map)
huffman_codes = huffman_encode(root)
original_text = ('A' * 45) + ('B' * 13) + ('C' * 12) + ('D' * 16) + ('E' * 9) + ('F' * 5)
full_encoded_str = "".join(huffman_codes[char] for char in original_text)

decoded_str = huffman_decode(root, full_encoded_str)
print(f"Freq map: {freq_map}")
print(f"Huffman code: {huffman_codes}")
print(f"Encoded string: {full_encoded_str}")
print(f"Decoded string: {decoded_str}")