class Node:
    def __init__(self,val):
        self.val = val
        self.left = None 
        self.right = None 
def allthreeTraversals(root):
    preorder = []
    postorder = []
    inorder = []
    stack =[ ]
    stack.append([root,1])
    while stack:
        poppedElement = stack.pop()
        if poppedElement[1] == 1:
            poppedElement[1] = 2
            inorder.append(poppedElement[0].val)
            stack.append(poppedElement)
            if poppedElement[0].left:
                stack.append([poppedElement[0].left,1])
        elif poppedElement[1] == 2:
            poppedElement[1] = 3
            preorder.append(poppedElement[0].val)
            stack.append(poppedElement)
            if poppedElement[0].right:
                stack.append([poppedElement[0].right,1])
        else:
            postorder.append(poppedElement[0].val)
    print("Inorder",inorder)
    print("Postorder",postorder)
    print("Preorder",preorder)







root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
allthreeTraversals(root)