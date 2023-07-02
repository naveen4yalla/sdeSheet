class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        #create an adjancy list
        edges = defaultdict(list)
        for i,j in prerequisites:
            edges[i].append(j)
        
        #dfs
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for pre in edges[crs]:
                    prereqMap[crs] |= dfs(pre)
            prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap = {} # map course -> set indirect prereqs
        for crs in range(numCourses):
            dfs(crs)
        
        result = []
        for i , j in queries:
            result.append(j in prereqMap[i])
        return result
            
            
            
        