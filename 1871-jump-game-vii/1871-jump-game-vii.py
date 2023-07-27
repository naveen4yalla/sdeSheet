class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        f = 0
        while q:
            i = q.popleft()
            start = max(minJump+ i , f+1)
            for j in range(start,min(i+maxJump+1,len(s))):
                if s[j] == "0":
                    q.append(j)
                    if j == len(s)-1:
                        return True
            f = i + maxJump
        return False