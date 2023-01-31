from collections import deque
class Solution:
    def widthOfBinaryTree(self, root):
        queue = deque()
        ans = 0
        if root is not None:
            queue.append([root,0])
        while queue:
            left,right = None, None
            curmin = queue[0][1]
            n = len(queue)
            for f in range(n):
                temp = queue[0] 
                queue.popleft()
                if f == 0:
                    left = temp[1] -curmin
                if f == n-1:
                    right = temp[1] - curmin
                if temp.left:
                    queue.append([temp,2*curmin+1])
                if temp.right:
                    queue.append([temp,2*curmin+2])
            ans = max(ans,right-left +1)
        return ans
    
                     