class Solution:
    def zigzagLevelOrder(self,root):
        if root == None:
            return []
        queue = []
        queue.append(root)
        shiftTraversal = False
        result = []
       
        while queue:
            temp = []
            i = len(queue)
            for f in range(0,i):
                popElement = queue.pop(0)
                if shiftTraversal == True:
                    temp.insert(0,popElement.val)
                else:
                    temp.append(popElement.val)
                if popElement.left:
                    queue.append(popElement.left)
                if popElement.right:
                    queue.append(popElement.right)
            shiftTraversal = not shiftTraversal
            result.append(temp)
        return result