class Solution:
    def exist(self,board,word):
        rows , cols = len(board) , len(board[0])
        visited = set()
        def dfs(r,c,index):
            if index == len(word):
                return True
            if 0<=r<rows and  0<=c<cols and word[index] == board[r][c] and (r,c) not in visited:
                visited.add((r,c))
                result = (dfs(r,c+1,index+1) or
                dfs(r,c-1,index+1) or
                dfs(r+1,c,index+1) or
                dfs(r-1,c,index+1))
                visited.remove((r,c))
            else:
                return False
            return result
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
                   