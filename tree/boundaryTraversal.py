class Solution:
    def __init__(self):
        self.result = []
    def boundaryOfBinaryTree(self, root):
        if root is  None:
            return []
        if self.checkLeaf(root) is True:
            self.result.append(root.val)
            return self.result
        self.result.append(root.val)
        self.leftSide(root.left)
        self.leafNodes(root)
        self.rightSide(root.right)
        return self.result
    
    def leftSide(self,root):
        while root:
            if self.checkLeaf(root) is  not True:
                self.result.append(root.val)
                #self.leftSide(root.left)
            if root.left:
                root = root.left
            else:
                root = root.right
    def rightSide(self,root):
        temp = []
        while root:
            if self.checkLeaf(root) is not True:
                temp.append(root.val)
            if root.right:
                root = root.right
            else:
                root = root.left
        temp.reverse()
        self.result = self.result + temp
    

    def leafNodes(self,root):
        if self.checkLeaf(root) is True:
            self.result.append(root.val)
        if root.left:
            self.leafNodes(root.left)
        if root.right:
            self.leafNodes(root.right)
    def checkLeaf(self,root):
        if root.left == None and root.right == None:
            return True

