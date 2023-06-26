class Solution(object):
    def openLock(self, deadends, target):
        def neighbors(node):
            result = []
            for i in range(4):
                digit = str((int(node[i]) + 1) % 10)
                result.append(node[:i]+digit+node[i+1:])
                digit = str((int(node[i]) -1 + 10) % 10)
                result.append(node[:i]+digit+node[i+1:])
            return result
                
                

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1
        