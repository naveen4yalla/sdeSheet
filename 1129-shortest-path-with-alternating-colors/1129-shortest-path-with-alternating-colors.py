from collections import deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Create adjacency lists for red and blue edges
        red_adjacency = [[] for _ in range(n)]
        blue_adjacency = [[] for _ in range(n)]
        
        # Build adjacency lists for red edges
        for src, dest in redEdges:
            red_adjacency[src].append(dest)
        
        # Build adjacency lists for blue edges
        for src, dest in blueEdges:
            blue_adjacency[src].append(dest)
        
        # Initialize result array with -1 for unreachable nodes
        result = [-1] * n
        
        # Initialize the queue for BFS traversal
        queue = deque()
        
        # Initialize starting node as 0 (source)
        queue.append((0, None, 0))
        visited = set()
        visited.add((0,None))
        # Perform BFS traversal
        while queue:
            node, color, distance = queue.popleft()
            
            # Update result if the node is unvisited or a shorter path is found
            if result[node] == -1 or result[node]>distance:
                result[node] = distance
                
            if color!='red':
                for neighbor in red_adjacency[node]:
                    if (neighbor,'red') not in visited:
                        queue.append((neighbor, 'red', distance + 1))
                        visited.add((neighbor,'red'))
            if color!='blue':
                for neighbor in blue_adjacency[node]:
                    if (neighbor,'blue') not in visited:
                        queue.append((neighbor, 'blue', distance + 1))
                        visited.add((neighbor,'blue'))
        
        return result
