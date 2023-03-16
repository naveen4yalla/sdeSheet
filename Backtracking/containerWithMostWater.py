class Solution:
    def maxArea(self,height):
        res = 0
        for left in range(len(height)):
            for right in range(left+1,len(height)):
                area = (right-left) * min(height[left],height[right])
                res = max(res,area)
        print(res)
s = Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])