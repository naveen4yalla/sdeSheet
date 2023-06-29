class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        #computing left prefix table
        self.prefix = [0] * len(nums)
        temp = 0
        for i in range(len(nums)):
            self.prefix[i] = temp + nums[i]
            temp = temp + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        #
        r = self.prefix[right]
        l = self.prefix[left -1] if left > 0 else 0
        return r-l

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)