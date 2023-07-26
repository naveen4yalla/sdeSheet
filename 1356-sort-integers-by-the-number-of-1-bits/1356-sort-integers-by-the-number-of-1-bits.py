class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ls =[]
        heapq.heapify(ls)
        result = []
        for i in arr:
            heapq.heappush(ls,[count_set_bits(i),i])
        while ls:
            _ , value = heapq.heappop(ls)
            result.append(value)
        return result
            

        
def count_set_bits(num):
    count = 0
    while num:
        count += num & 1  
        num >>= 1
    return count
        