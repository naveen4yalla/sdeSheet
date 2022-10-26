class Node:
    def __init__(self,val):
        self.val = val
        self.left = None 
        self.right = None
def rootToNode(root,ans,node):
    if root:
        ans.append(root.val)
    if root == None:
        return False
    if root == node:
        return True
    if rootToNode(root.left,ans,node) or rootToNode(root.right,ans,node):
        return True
    ans.pop()
    return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)
ans = []
rootToNode(root,ans,root.left.right.right)
print(ans)