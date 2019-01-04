class Node:
    def __init__(self):
        self.chars = [None]*26
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        ptr = self.trie
        for w in word:
            i = ord(w) - ord('a')
            if not ptr.chars[i]:
                ptr.chars[i] = Node()
            ptr = ptr.chars[i]
        ptr.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        ptr = self.trie
        for w in word:
            i = ord(w) - ord('a')
            if not ptr.chars[i]:
                return False
            ptr = ptr.chars[i]
        return ptr.end   

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        ptr = self.trie
        for w in prefix:
            i = ord(w) - ord('a')
            if not ptr.chars[i]:
                return False
            ptr = ptr.chars[i]
        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
