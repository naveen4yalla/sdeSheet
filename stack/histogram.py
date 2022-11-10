class Solution:
    def __init__(self,n):
        self.left  = [n] * 0
        self.right = [n] * 0
    def histogram(arr):
        stack= []
        for i  in range(len(arr)):
            while stack and stack[-1]>=arr[i]:
                stack.pop()
            if stack:
                self.left[i] = 0
            else:
                self.right[i] = stack[-1] + 1
            stack.push[i]
         for i  in range(len(arr),-1,-1):
            while stack and stack[-1]>=arr[i]:
                stack.pop()
            if stack:
                self.left[i] = i - 1
            else:
                self.right[i] = stack[-1] - 1
            stack.push[i]

arr = [2,1,5,6,2,3]
s= Solution(len(arr))
s.histogram(arr)
