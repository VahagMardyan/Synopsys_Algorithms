from rbt import Red_Black_Tree, Node

r = Red_Black_Tree()
nums = [10, 20, 30, 15, 25, 5, 1]

for n in nums:
    # print(f"\nAdding {n}:")
    r.insert(Node(n))

r.display()

print()
r.insert(Node(4))
r.display()

r.delete(r.search(4))
r.display()

# r = Red_Black_Tree()
# for n in [10, 20, 30]:
#     r.insert(Node(n))

# print(r.is_valid_tree()) # Should be True

# if r.root.left:
#     r.root.left.color = True # # breaks 5th rule (const black-height)

# print(r.is_valid_tree()) # False