class Solution:
     def subsetswithDup(self, nums)
         res = []
         nums. sort ()
         def backtrack (i, subset):
             if i == len (nums):
                 res. append(subset[::)]
                 return
             # All subsets that include nums[i]
            subset. append (nums [i])
            backtrack(i + 1, subset)
            subset. pop()
             # All subsets that don't include nums [i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)
