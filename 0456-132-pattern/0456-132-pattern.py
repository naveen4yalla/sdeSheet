class Solution:
    def find132pattern(self, nums):
        stack = []
        curmin = nums[0]
        for i in nums[1:]:
            while stack and i >= stack[-1][1]:
                stack.pop()
            if stack and i > stack[-1][0]:  # Fixed the variable name here from 'n' to 'i'
                return True
            stack.append((curmin, i))
            curmin = min(curmin, i)
        return False

        
        