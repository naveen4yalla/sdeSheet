from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        counter = defaultdict(int)
        result = 0
        for right in range(len(fruits)):
            counter[fruits[right]] = counter[fruits[right]] + 1
            while len(counter) > 2:
                counter[fruits[left]]-=1
                if not counter[fruits[left]]:
                    del counter[fruits[left]]
                left+=1
            result = max(result,right-left+1)
        
        return result
            
        
        
        