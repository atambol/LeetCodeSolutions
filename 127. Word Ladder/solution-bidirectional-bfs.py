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

        # bidirectional BFS
        # maintain visited dictionaries (node -> count)
        v1 = {}
        v2 = {}
        
        # queue for search
        q1 = [beginWord]
        q2 = [endWord]
        
        # count of depth
        c1 = 1
        c2 = 1
        
        # bfs from both sides
        while q1 or q2:
            # bfs on q1
            n1 = []
            for node in q1:
                # should not revisit in this BFS
                if node in v1:
                    continue
                    
                # found overlap
                if node in v2:
                    return c1 + v2[node] - 1
                
                # mark visited
                v1[node] = c1
                
                # add neighbours
                n1.extend(graph[node])
            q1 = n1
            c1 += 1
            
            # bfs on q2
            n2 = []
            for node in q2:
                # should not revisit in this BFS
                if node in v2:
                    continue
                    
                # found overlap
                if node in v1:
                    return c2 + v1[node] - 1
                
                # mark visited
                v2[node] = c2
                
                # add neighbours
                n2.extend(graph[node])
            q2 = n2
            c2 += 1
            
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
        
