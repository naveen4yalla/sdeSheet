class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode("")
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

        node.counter += 1
        
    def dfs(self, node, prefix):
        if node.is_end:
            self.output.append(prefix)
        
        for char in node.children:
            self.dfs(node.children[char], prefix + char)
    
    def query(self, x):
        self.output = []
        node = self.root
        
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.dfs(node, x)
        return self.output

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        T = Trie()
        result = []
        
        for i in products:
            T.insert(i)
        
        prefix = ""
        for j in searchWord:
            prefix += j
            temp = T.query(prefix)
            temp.sort()  # Sort the suggestions lexicographically
            if len(temp) > 3:
                temp = temp[:3]  # Get the first three lexicographically minimum products
            result.append(temp)
        
        return result

