from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Create adjacency list and indegrees array
        adjacency = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        # Step 2: Populate adjacency list and indegrees array
        for course, prerequisite in prerequisites:
            adjacency[prerequisite].append(course)
            indegrees[course] += 1

        # Step 3: Perform topological sort
        q = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)

        result = []
        while q:
            curr = q.popleft()
            result.append(curr)
            for course in adjacency[curr]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    q.append(course)

        # Step 4: Check if all courses can be taken
        if len(result) == numCourses:
            return result
        else:
            return []
            
        
        