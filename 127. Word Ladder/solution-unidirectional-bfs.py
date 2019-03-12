class Solution:
    def __init__(self):
        self.graph = {}
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # create a graph
        wordList.append(beginWord)
        for w in wordList:
            self.graph[w] = []
            
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if self.isOneEdit(wordList[i], wordList[j]):
                    self.graph[wordList[i]].append(wordList[j])
                    self.graph[wordList[j]].append(wordList[i])
        
        # bfs to end word
        visited = set()
        return self.bfs(visited, [beginWord], endWord)
    
    def bfs(self, visited, queue, end):
        count = 1
        while queue:
            newqueue = []
            for node in queue:
                if node in visited:
                    continue
                if node == end:
                    return count
                visited.add(node)
                newqueue.extend(self.graph[node])
            count += 1
            queue = []
            for node in newqueue:
                if node not in visited:
                    queue.append(node)
        return 0
            
    def isOneEdit(self, w1, w2):
        diff = 0
        for i in range(len(w1)):
            if w2[i] != w1[i]:
                diff += 1
                if diff > 1:
                    return False
                
        return True
