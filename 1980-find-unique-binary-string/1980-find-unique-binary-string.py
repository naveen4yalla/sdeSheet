class Solution:
    def findDifferentBinaryString(self, nums):
        n = len(nums[0])
        binary_strings = set(nums)

        for i in range(2 ** n):
            binary_string = bin(i)[2:].zfill(n)
            if binary_string not in binary_strings:
                return binary_string