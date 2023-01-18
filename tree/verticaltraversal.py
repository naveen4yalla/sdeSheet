from collections import deque,OrderedDict
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None 
        self.right = None 



def verticalTraversals(root):
    queue = deque([(root, 0, 0)])
    bfsnodes = []
    while queue:
        poppedElement=queue.popleft()
        if poppedElement[0]:
            bfsnodes.append([poppedElement[2],poppedElement[1],poppedElement[0].val])
            if poppedElement[0].left:
                queue.append([poppedElement[0].left,poppedElement[1]+1,poppedElement[2]-1])
            if poppedElement[0].right:
                queue.append([poppedElement[0].right,poppedElement[1]+1,poppedElement[2]+1])
    bfsnodes.sort()
    #print(bfsnodes)
    ret = OrderedDict()
    
    for column, row, value in bfsnodes:
        if column in ret:
            ret[column].append(value)
        else:
            ret[column] = [value]
    print(ret)
    return ret.values()







root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
print(verticalTraversals(root))