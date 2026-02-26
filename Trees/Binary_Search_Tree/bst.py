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

    def _transplant(self, u:Node, v:Node):
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
            self._transplant(z,z.right)
        elif z.right is None:
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z,y)
            y.left = z.left
            y.left.parent = y

    def inorder(self):
        """
        Inorder -> left, root, right
        """
        self.__inorder_helper(self.root)
        print()

    def iterative_inorder(self):
        print("Iterative Inorder:", end=" ")
        stack = []
        current = self.root

        while current is not None or stack:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                print(node.val, end=" ")
                current = node.right
    
    def preorder(self):
        """
        Preorder -> root, left, right
        """
        self.__preorder_helper(self.root)
        print()
    
    def iterative_preorder(self):
        print("Iterative Preorder:", end=" ")
        if self.root is None:
            return
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.val, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def postorder(self):
        """
        Postorder -> left, right, root
        """
        self.__postorder_helper(self.root)
        print()

    def iterative_postorder(self):
        print("Iterative Postorder: ", end=" ")
        if self.root is None:
            return
        stack = [self.root]
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

    def successor(self, x:Node = "not_given"):
        """
        Finds the smallest node greater than the given node.
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
        Finds the largest node less than given node.
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
    
    def __get_depth(self, node:Node) -> int:
        depth = 0
        while node.parent is not None:
            node = node.parent
            depth += 1
        return depth
    
    def LCA(self, u:Node, v:Node) -> Node:
        """
        Lowest Common Ancestor
        """
        if u is None or v is None:
            return None
        
        d1 = self.__get_depth(u)
        d2 = self.__get_depth(v)

        diff = abs(d1 - d2)
        if d1 > d2:
            for _ in range(diff):
                u = u.parent
        else:
            for _ in range(diff):
                v = v.parent

        while u != v:
            u = u.parent
            v = v.parent
        return u
    
    def display(self):
        print("\n--- BST Structure ---")
        self.__print_tree(self.root, 0)
        print("---------------------\n")

    def __print_tree(self, node:Node, level:int) -> None:
        if node is not None:
            self.__print_tree(node.right, level+1)
            print(" " * 8 * level + "->", node.val)
            self.__print_tree(node.left, level+1)

    def is_valid_tree(self) -> bool:
        return self.__is_valid_helper(self.root, float("-inf"), float("inf"))

    def __is_valid_helper(self, node:Node, min_val, max_val) -> bool:
        if node is None:
            return True
        if not (min_val < node.val < max_val):
            return False
        return self.__is_valid_helper(node.left, min_val, max_val) and \
               self.__is_valid_helper(node.right, min_val, max_val)
    
def LCA_binary_search_tree(node:Node, u:Node, v:Node) -> Node:
    """
    Lowest Common Ancestor
    """
    if node is None:
        return None
    
    if u.val <= node.val and v.val <= node.val:
        return LCA_binary_search_tree(node.left, u, v)
    
    if u.val >= node.val and v.val >= node.val:
        return LCA_binary_search_tree(node.right, u, v)

    return node

# r = BinarySearchTree()

# for val in [100, 20, 200, 10, 30, 150, 300]:
#     r.insert(val)

# for val in [9, 7, 15, 4, 8, 2, 5, 10, 17]:
#     r.insert(val)

# r.delete(r.search(17))

# print("Inorder: ")
# r.iterative_inorder()
# print()
# r.inorder()

# print("Preorder: ")
# r.iterative_preorder()
# print()
# r.preorder()

# print("Postorder: ")
# r.iterative_postorder()
# print()
# r.postorder()

# print(f"Found: {r.search(15).val}")

# print("Min:",r.minimum().val)
# print("Max:",r.maximum().val)
# print("Successor:", r.successor().val) # # root:9 ->  10
# print("Predecessor:", r.predecessor().val) # # root:9 -> 8

# print(r.search(25))
# print(r.successor(r.search(35)))
# print(r.successor(r.search(28)))

# lca = r.LCA(r.search(2), r.search(8))

# print(lca.val)

# r.insert(18)

# r.delete(r.search(15))
# r.preorder()

# r.display()