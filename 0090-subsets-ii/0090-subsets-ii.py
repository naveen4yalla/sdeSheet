class Solution:
    def subsetsWithDup(self, nums):
        result = []
        n = len(nums)
        nums.sort()
        def util(index,arr):
            result.append(list(arr))
            num = float("-inf")
            for f in range(index,n):
                #if f!=index and nums[f-1] == nums[f]:
                    #continue
                if num!=nums[f]:
                    num = nums[f]
                    arr.append(nums[f])
                    util(f+1,arr)
                    arr.pop()
        util(0,[])
        return result