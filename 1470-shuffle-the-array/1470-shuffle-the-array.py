class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n // 2):
            res.append(nums[i])
            res.append(nums[i + n // 2])
        return res