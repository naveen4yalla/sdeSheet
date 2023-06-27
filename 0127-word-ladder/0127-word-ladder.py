from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                nei[pattern].append(word)
        visit  = set(beginWord)
        q = deque([beginWord])
        result = 0
        while q:
            for i in range(len(q)):
                word  = q.popleft()
                if word == endWord:
                    return result+1
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            result+=1
        return 0