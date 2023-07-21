# class Solution:
#     def canCompleteCircuit(self,gas, cost):
#         n = len(gas)
#         for start in range(n):
#             tank = 0
#             for i in range(n):
#                 j = (start + i) % n
#                 tank += gas[j]
#                 if tank < cost[j]:
#                     break
#                 tank -= cost[j]
#             else:
#                 return start
#         return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        curr_gain = 0
        answer = 0
        
        for i in range(len(gas)):
            # gain[i] = gas[i] - cost[i]
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]

            # If we meet a "valley", start over from the next station
            # with 0 initial gas.
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1
        
        return answer if total_gain >= 0 else -1


        