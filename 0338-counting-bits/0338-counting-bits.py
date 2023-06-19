class Solution:
    def countBits(self, n: int) -> List[int]:
        
        mem = [0]*(n+1)
        
        if n == 0:
            return mem
        
        mem[0] = 0
        mem[1] = 1

        for i in range(2,n+1):
            
            if i%2 == 0:
                mem[i] = mem[i//2]
            
            else:
                mem[i] = mem[i//2] + 1
                
        
        return mem
		