class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_queue = deque()
        d_queue = deque()
        
        for i , j in enumerate(senate):
            if j == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
            
        while r_queue and d_queue:
            a = r_queue.popleft()
            b = d_queue.popleft()
            
            
            if a < b:
                r_queue.append(a+n)
            else:
                d_queue.append(b+n)
        return "Dire" if d_queue else "Radiant"
        