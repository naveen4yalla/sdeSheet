class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        left = 0
        right = 0
        total_sum = 0

        for right in range(len(arr)):
            if right - left + 1 > k:
                total_sum -= arr[left]
                left += 1
            total_sum += arr[right]

            if right - left + 1 == k and total_sum // k >= threshold:
                count += 1

        return count
                
        