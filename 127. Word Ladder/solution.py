class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int: 
        # edge case
        if beginWord == endWord or not wordList or endWord not in wordList:
            return 0
        
        # create a graph with neighbouring nodes of 1 edit difference
        wordList.append(beginWord)
        graph = {}
        for word in wordList:
            graph[word] = []
        
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if self.isOneEdit(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        # unidirectional BFS
        # maintain visited set
        visited = set()  
        q = [beginWord]
        count = 1
        while q:
            # bfs on q1
            newq = []
            for node in q:
                # should not revisit in this BFS
                if node in visited:
                    continue
                    
                # found overlap
                if node == endWord:
                    return count
                
                # mark visited
                visited.add(node)
                
                # add neighbours
                newq.extend(graph[node])
            q = newq
            count += 1
            
        return 0
            
        
    def isOneEdit(self, word1, word2):
        i = 0
        edits = 0
        
        while i < len(word1):
            if word1[i] != word2[i]:
                edits += 1
                if edits > 1:
                    return False
            i += 1
                
        if edits == 1:
            return True
        else:
            return False
        
