class Node:
    def __init__(self,val):
        self.val = val
        self.left = None 
        self.right = None 

def inorder(root):
    stack = []
    curr = root
    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left 
        elif(stack):
            curr= stack.pop()
            print(curr.val)
            curr = curr.right
        else:
            break
        





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inorder(root)