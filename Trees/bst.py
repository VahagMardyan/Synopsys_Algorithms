"""
Inorder -> left, root, right
Preorder -> root, left, right
Postorder -> left, right, root
"""

"""
__functionName -> like private functions in C++. Python renames it as _className__functionName
_functionName -> like protected functions in C++. You can use it, but be careful.
"""

class Node:
    """
    Node class for Binary Search Tree
    """
    def __init__(self,key):
        self.parent = None
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __inorder_helper(self, node:Node):
        if node:
            self.__inorder_helper(node.left)
            print(node.val, end=" ")
            self.__inorder_helper(node.right)

    def __preorder_helper(self, node:Node):
        if node:
            print(node.val, end=" ")
            self.__preorder_helper(node.left)
            self.__preorder_helper(node.right)

    def __postorder_helper(self, node:Node):
        if node:
            self.__postorder_helper(node.left)
            self.__postorder_helper(node.right)
            print(node.val, end=" ")

    def __transplant(self, u:Node, v:Node):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def height(self, x:Node = "not_given"):
        if x == "not_given":
            x = self.root
        if x is None:
            return -1
        left_h = self.height(x.left)
        right_h = self.height(x.right)
        return 1 + max(left_h, right_h)
    
    def search(self, k):
        current = self.root
        while current is not None and k != current.val:
            if k < current.val:
                current = current.left
            else:
                current = current.right
        return current if current else None
    
    def minimum(self, x:Node = "not_given"):
        if x == "not_given":
            x = self.root
        if x is None:
            return None
        current = x
        while current.left is not None:
            current = current.left
        return current
    
    def maximum(self, x:Node = "not_given"):
        if x == "not_given":
            x = self.root
        if x is None:
            return None
        current = x
        while current.right is not None:
            current = current.right
        return current

    def insert(self, key):
        z = Node(key)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.val < y.val:
            y.left = z
        else:
            y.right = z
    
    def delete(self, z:Node):
        if z is None:
            return
        
        if z.left is None:
            self.__transplant(z,z.right)
        elif z.right is None:
            self.__transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.__transplant(z,y)
            y.left = z.left
            y.left.parent = y

    def inorder(self):
        """
        Inorder -> left, root, right
        """
        self.__inorder_helper(self.root)
        print()
    
    def preorder(self):
        """
        Preorder -> root, left, right
        """
        self.__preorder_helper(self.root)
        print()

    def postorder(self):
        """
        Postorder -> left, right, root
        """
        self.__postorder_helper(self.root)
        print()

    def successor(self, x:Node = "not_given"):
        """
        Finds the smallest node greater than given x.
        """
        if x == "not_given":
            x = self.root

        if x is None:
            return None
        
        if x.right is not None:
            return self.minimum(x.right)
        
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x:Node = "not_given"):
        """
        Finds the largest node less than given x.
        """
        if x == "not_given":
            x = self.root

        if x is None:
            return None
        
        if x.left is not None:
            return self.maximum(x.left)
        
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y
    

def iterative_search(x:Node, k):
    while x is not None and k != x.val:
        if k < x.val:
            x = x.left
        else:
            x = x.right
    
    return x if x else None
        
def iterative_inorder(x:BinarySearchTree):
    stack = []
    current = x.root

    while current is not None or stack:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            node = stack.pop()
            print(node.val, end=" ")
            current = node.right

def iterative_preorder(x:BinarySearchTree):
    if x.root is None:
        return
    stack = [x.root]
    while stack:
        node = stack.pop()
        print(node.val, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
def iterative_postorder(x:BinarySearchTree):
    if x.root is None:
        return
    stack = [x.root]
    values = []
    while stack:
        node = stack.pop()
        values.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    values.reverse()
    for i in values:
        print(i, end=" ")

r = BinarySearchTree()

# for val in [100, 20, 200, 10, 30, 150, 300]:
#     r.insert(val)

for val in [9, 7, 15, 4, 8, 2, 5, 10, 17, 16]:
    r.insert(val)

# r.delete(r.search(17))

print("Inorder: ")
iterative_inorder(r)
print()
r.inorder()

print("Preorder: ")
iterative_preorder(r)
print()
r.preorder()

print("Postorder: ")
iterative_postorder(r)
print()
r.postorder()

print(f"Found: {r.search(15).val}")
print(iterative_search(r.root, 15).val)

print("Min:",r.minimum().val)
print("Max:",r.maximum().val)
print("Successor:", r.successor().val) # # root:9 ->  10
print("Predecessor:", r.predecessor().val) # # root:9 -> 8

print(r.search(25))
print(r.successor(r.search(35)))
print(r.successor(r.search(28)))

