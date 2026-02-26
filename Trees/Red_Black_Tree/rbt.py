class Node:
    """
    Node class for Red-Black-Tree
    """
    def __init__(self, key):
        self.val = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = False # False for RED, True for Black
        self.height = 0
    

class Red_Black_Tree:
    """
    Rules.
        1. Every node is either RED or BLACK
        2. Root is always BLACK
        3. Each leaf (None or NIL) is BLACK
        4. If the node is RED then its children must be BLACK
        5. Any path from node to leaf must contain the same amount of BLACK nodes (Black-Height)
    """
    def __init__(self):
        self.root = None

    def __get_height(self, node:Node):
        return node.height if node else -1
    
    def __update_height(self, node:Node):
        if node:
            node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def left_rotate(self, z:Node) -> None:
        y = z.right
        z.right = y.left
        if y.left is not None:
            y.left.parent = z
        y.parent = z.parent
        if z.parent is None:
            self.root = y
        elif z == z.parent.left:
            z.parent.left = y
        else:
            z.parent.right = y
        y.left = z
        z.parent = y

        self.__update_height(y)
        self.__update_height(z)

    def right_rotate(self, z:Node) -> None:
        y = z.left
        z.left = y.right
        if y.right is not None:
            y.right.parent = z
        
        y.parent = z.parent
        if z.parent is None:
            self.root = y
        elif z == z.parent.right:
            z.parent.right = y
        else:
            z.parent.left = y
        
        y.right = z
        z.parent = y

        self.__update_height(y)
        self.__update_height(z)


    def __insert_fixup(self, z:Node):
        while z.parent and z.parent.parent and z.parent.color == False:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right # # uncle

                # case1: uncle is "RED"
                if y and y.color == False:
                    z.parent.color = True
                    y.color = True
                    z.parent.parent.color = False
                    z = z.parent.parent
                else:
                    # case2: uncle is "BLACK" and z is the right-child
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    
                    # case3: uncle is "BLACK" and z is the left-child
                    z.parent.color = True
                    z.parent.parent.color = False
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left # uncle

                # case4: uncle is "RED"
                if y and y.color == False:
                    z.parent.color = True
                    y.color = True
                    z.parent.parent.color = False
                    z = z.parent.parent
                else:
                    # case5: uncle is "BLACK" and z is the left-child
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    
                    # case6: uncle is "BLACK" and z is the right-child
                    z.parent.color = True
                    z.parent.parent.color = False
                    self.left_rotate(z.parent.parent)
        self.root.color = True
    
    def insert(self, z:Node):
        x = self.root
        y = None
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
        z.left = None
        z.right = None
        z.color = False

        temp = z
        while temp is not None:
            self.__update_height(temp)
            temp = temp.parent
        
        self.__insert_fixup(z)

    def display(self, node:Node = None, indent = "", last = True):
        if node is None:
            node = self.root
        
        if node is not None:
            print(indent, end="")
            if last:
                print("└─", end="")
                indent += "  "
            else:
                print("├─", end="")
                indent += "| "
            color = "BLACK" if node.color else "RED"
            print(f"{node.val}({color})")

            children = []
            if node.left:
                children.append((node.left, False if node.right else True))
            if node.right:
                children.append((node.right, True))
            
            for i, (child, is_last) in enumerate(children):
                self.display(child, indent, is_last)

    def __transplant(self, u:Node, v:Node):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, z: Node):
        y = z
        y_original_color = y.color
        if z.left is None:
            x = z.right
            self.__transplant(z, z.right)
            parent_to_update = z.parent
        elif z.right is None:
            x = z.left
            self.__transplant(z, z.left)
            parent_to_update = z.parent
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                if x is not None:
                    x.parent = y
                parent_to_update = y
            else:
                parent_to_update = y.parent
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            
            self.__transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        temp = parent_to_update
        while temp is not None:
            self.__update_height(temp)
            temp = temp.parent

        if y_original_color == True:
            self.__delete_fixup(x, parent_to_update)

    def __delete_fixup(self, x: Node, parent: Node):
        while x != self.root and (x is None or x.color == True):

            if x == parent.left or (x is None and parent.left is None):
                w = parent.right
                if w and w.color == False:
                    w.color = True
                    parent.color = False
                    self.left_rotate(parent)
                    w = parent.right
                
                if w and (not w.left or w.left.color == True) and (not w.right or w.right.color == True):
                    w.color = False
                    x = parent
                    parent = x.parent if x else None
                else:
                    if w and (not w.right or w.right.color == True):
                        if w.left: w.left.color = True
                        w.color = False
                        self.right_rotate(w)
                        w = parent.right
                    if w:
                        w.color = parent.color
                        parent.color = True
                        if w.right: w.right.color = True
                        self.left_rotate(parent)
                    x = self.root
            else: # Mirror Case
                w = parent.left
                if w and w.color == False:
                    w.color = True
                    parent.color = False
                    self.right_rotate(parent)
                    w = parent.left
                if w and (not w.left or w.left.color == True) and (not w.right or w.right.color == True):
                    w.color = False
                    x = parent
                    parent = x.parent if x else None
                else:
                    if w and (not w.left or w.left.color == True):
                        if w.right: w.right.color = True
                        w.color = False
                        self.left_rotate(w)
                        w = parent.left
                    if w:
                        w.color = parent.color
                        parent.color = True
                        if w.left: w.left.color = True
                        self.right_rotate(parent)
                    x = self.root
        if x: x.color = True    

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
    
    def search(self, k):
        current = self.root
        while current is not None and k != current.val:
            if k < current.val:
                current = current.left
            else:
                current = current.right
        return current
    
    def height(self, x:Node = "not_given"):
        if x == "not_given":
            x = self.root
        if x is None:
            return -1
        return x.height
    
    def black_height(self, x:Node = None):
        if x is None:
            x = self.root
        h = 1 # None (Nil) is included
        current = x
        while current is not None:
            if current.color == True:
                h += 1
            current = current.left
        return h
    
    def is_valid_tree(self) -> bool:
        if self.root is None:
            return True
        
        # Second rule: Root is always "BLACK"
        if self.root.color == False:
            return False
        
        target_black_height = self.black_height(self.root)

        return self.__check_rules(self.root, 0, target_black_height)
    
    def __check_rules(self, node:Node, current_black_count:int, target_bh:int):
        if node is None:
            # # When we reach to None (NIL), check rule 5 (NIL Included)
            return current_black_count + 1 == target_bh
        
        # Rule 4: RED node can't have RED child
        if node.color == False:
            if (node.left and node.left.color == False) or (node.right and node.right.color == False):
                return False
            
        new_black_count = current_black_count + (1 if node.color == True else 0)

        return self.__check_rules(node.left, new_black_count, target_bh) and \
               self.__check_rules(node.right, new_black_count, target_bh)
        
