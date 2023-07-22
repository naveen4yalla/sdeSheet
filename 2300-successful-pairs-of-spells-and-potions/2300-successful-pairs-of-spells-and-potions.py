class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result = []
        for s in spells:
            left , right = 0 ,len(potions) - 1
            idx = len(potions)
            
            while left <= right:
                mid = left + ((right -left) // 2)
                if s * potions[mid] >= success:
                    right = mid -1
                    idx = mid
                else:
                    left = mid + 1
            result.append(len(potions) - idx)
        return result