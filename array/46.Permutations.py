#use a decision tree in python 
class Solution:
    def permute(self, nums):
        result = []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for p in perms:
                p.append(n)
            result.extend(perms)
            nums.append(n)
        return result