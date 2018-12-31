class Node:
    def __init__(self):
        self.char = {}
        self.ends = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        ptr = self.map
        for w in word:
            if w in ptr.char:
                ptr = ptr.char[w]
            else:
                node = Node()
                ptr.char[w] = node
                ptr = ptr.char[w]
        ptr.ends = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        ptr = self.map
        for w in word:
            if w in ptr.char:
                ptr = ptr.char[w]
            else:
                return False
        return ptr.ends

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        ptr = self.map
        for w in prefix:
            if w in ptr.char:
                ptr = ptr.char[w]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
