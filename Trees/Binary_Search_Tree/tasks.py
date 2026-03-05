from binary_search_tree import Binary_Search_Tree, Node_bst

"""
1. Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return nul
"""

def find_subtree(r:Binary_Search_Tree, value):
    current = r.root
    if current is None:
        return None
    
    while current is not None and current.val != value:
        if value < current.val:
            current = current.left
        else:
            current = current.right
    return current

"""
2. Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST
is changed to the original key plus the sum of all keys greater than the original key in BST
"""

def convert(r:Binary_Search_Tree):
    stack = []
    current = r.root
    s = 0
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.right
        current = stack.pop()
        s += current.val
        current.val = s
        current = current.left

r = Binary_Search_Tree()
for val in [9, 7, 13, 3, 8, 2, 5, 10, 17]:
    r.insert(val)

result_node = find_subtree(r, 7)

# if result_node:
#     print(result_node.val)
#     if result_node.left:
#         print(result_node.left.val)
#     if result_node.right:
#         print(result_node.right.val)

# r.preorder()
# convert(r)
# r.preorder()

"""
3. Given the root of a binary tree, return the number of nodes where the value of 
the node is equal to the average of the values in its subtree.
"""

def dfs(node:Node_bst):
    if node is None:
        return 0,0,0
    
    left_sum, left_count, left_res = dfs(node.left)
    right_sum, right_count, right_res = dfs(node.right)

    current_sum = node.val + left_sum + right_sum
    current_count = 1 + left_count + right_count
    current_res = left_res + right_res

    if node.val == current_sum // current_count:
        current_res += 1
    
    return current_sum, current_count, current_res

sm, cnt, result = dfs(r.search(13))
# print(sm, cnt, result) # 40 3 3

r = Binary_Search_Tree()

for val in [15,18,17,20,6,3,7,13,9,2,4]:
    r.insert(val)

# r.display()
r.insert(14)

def recursive_minimum(x:Node_bst) -> Node_bst:
    if x is None:
        return None

    if x.left is None:
            return x
        
    return recursive_minimum(x.left)

def recursive_maximum(x:Node_bst) -> Node_bst:
    if x is None:
        return None
    
    if x.right is None:
        return x
    
    return recursive_maximum(x.right)

print(r.minimum().val)
print(recursive_minimum(r.root).val)

print(r.maximum().val)
print(recursive_maximum(r.root).val)

def is_valid_BST(node) -> bool:
    if node is None:
        return True
    
    if hasattr(node, 'root'):
        node = node.root
        if node is None:
            return True
    
    if node.left and node.left.val >= node.val:
        return False
    
    if node.right and node.right.val <= node.val:
        return False
    
    return is_valid_BST(node.left) and is_valid_BST(node.right)

# print(is_valid_BST(r))

def is_valid(tree) -> bool:
    stack = []
    values = []
    current = tree.root
    while current is not None or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            node = stack.pop()
            values.append(node.val)
            current = node.right
    
    for i in range(len(values)):
        if values[i+1] >= values[i]:
            return True
    
    return False

# print(is_valid(r)) 

# r.display()

# r.delete(r.search(6))
# r.display()

# # print(r.predecessor(r.search(13)).val)
# # print(r.minimum(r.search(13)).val)

# r = BinarySearchTree()

# for val in [100, 20, 200, 10, 30, 150, 300]:
#     r.insert(val)

# for val in [9, 7, 15, 4, 8, 2, 5, 10, 17]:
#     r.insert(val)

# r.reversed_inorder()
# r.iterative_reversed_inorder()

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