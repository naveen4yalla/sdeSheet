class Node:
    def __init__(self,val):
        self.val = val
        self.left = None 
        self.right = None 
def morrispreorder(root):
    curr = root
    morrispreorderstack = []
    while curr:
        if curr.left == None:
            morrispreorderstack.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right != None and prev.right != curr:
                prev = prev.right
            if prev.right == None:
                prev.right = curr
                morrispreorderstack.append(curr.val)
                curr = curr.left
            else:
                prev.right = None
                curr = curr.right
    return morrispreorderstack

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
print(morrispreorder(root))