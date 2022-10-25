class Node:
    def __init__(self,val):
        self.val = val
        self.left = None 
        self.right = None 

def preorder(root):
    stack = []
    curr = root
    stack.push(curr)
    while stack:
        temp = stack.pop()
        print(temp.val)
        if temp.right:
            stack.push(temp.right)
        if temp.left:
            stack.push(temp.left)
            





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
preorder(root)