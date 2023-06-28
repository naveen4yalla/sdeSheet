from collections import defaultdict,Counter,deque
class Solution:
    
    def alienOrder(self, words: List[str]) -> str:

        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})


        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else: 
                if len(second_word) < len(first_word): return ""
        stack=[]
        output=[]
        for f,n in in_degree.items():
            if n==0:
                stack.append(f)
        while stack:
            #DFS
            node = stack.pop()
                # add popped element from stack to final order
            output.append(node)

            for course in adj_list[node]:
                in_degree[course] -= 1 #one less prerequisite
                if in_degree[course] == 0:
                    stack.append(course) #if all prerequisites done, add to stack
        if len(output) == len(in_degree):
            return "".join(output)
        else:
            return ""