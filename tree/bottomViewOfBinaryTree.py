from collections import OrderedDict
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None 
        self.right = None
def bottomView(root):
    queue = []
    queue.append([root,0])
    ls = {}
    while queue:
        poppedElement = queue.pop(0)
        ls[poppedElement[1]] = poppedElement[0].val
        if poppedElement[0].left:
            queue.append([poppedElement[0].left,poppedElement[1]-1])
        if poppedElement[0].right:
            queue.append([poppedElement[0].right,poppedElement[1]+1])
    ls = OrderedDict(sorted(ls.items()))
    print(ls.values())


        


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
bottomView(root)