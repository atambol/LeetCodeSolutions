from collections import defaultdict

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.chars = {}
        self.eow = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if not word[0] in self.chars:
            self.chars[word[0]] = Trie()
            
        if len(word) == 1:
            self.chars[word[0]].eow = True
        else:
            self.chars[word[0]].insert(word[1:])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            return self.eow
        else:
            if word[0] in self.chars:
                return self.chars[word[0]].search(word[1:])
            else:
                return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if len(prefix) == 1:
            if prefix[0] in self.chars:
                return True
            else:
                return False
        else:
            if prefix[0] in self.chars:
                return self.chars[prefix[0]].startsWith(prefix[1:])
            else:
                return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
