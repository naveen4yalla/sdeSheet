class Solution:
    def minKBitFlips(self,nums, k):
        n = len(nums)
        flips = 0
        flip_count = [0] * n  # A list to keep track of the number of flips at each position

        for i in range(n):
            if i >= k:
                flips ^= flip_count[i - k]  # If the window moves, remove its contribution
            if (nums[i] + flips) % 2 == 0:
                if i + k > n:
                    return -1  # If it's not possible to flip the entire window, return -1
                flips ^= 1
                flip_count[i] = 1

        return sum(flip_count)
            
        
        