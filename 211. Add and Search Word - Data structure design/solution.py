class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tries = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        n = len(word)
        if not n:
            return
        
        if n not in self.tries:
            self.tries[n] = {}
        trie = self.tries[n]
        
        for w in word:
            if w not in trie:
                trie[w] = {}
            trie = trie[w]
            

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        n = len(word)
        if not n:
            return False
        if n in self.tries:
            trie = self.tries[n]
            return self.dfs(word, trie)
        else:
            return False

    def dfs(self, word, trie):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        
        if word[0] == '.':
            for c in trie:
                if self.dfs(word[1:], trie[c]):
                    return True
            return False
        else:
            if word[0] not in trie:
                return False
            else:
                return self.dfs(word[1:], trie[word[0]])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
