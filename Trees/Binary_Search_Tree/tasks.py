from bst import BinarySearchTree, Node

"""
1. Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return nul
"""

def find_subtree(r:BinarySearchTree, value):
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

def convert(r:BinarySearchTree):
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

r = BinarySearchTree()
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

def dfs(node:Node):
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

r = BinarySearchTree()

for val in [15,18,17,20,6,3,7,13,9,2,4]:
    r.insert(val)

# r.display()
r.insert(14)

# r.display()

r.delete(r.search(6))
r.display()

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