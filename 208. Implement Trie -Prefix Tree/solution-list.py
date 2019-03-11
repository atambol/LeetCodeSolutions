class Node:
    def __init__(self):
        self.chars = [None]*26
        self.eow = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ptr = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self.ptr
        for char in word:
            i = ord(char) - ord('a')
            if not ptr.chars[i]:
                ptr.chars[i] = Node()
            ptr = ptr.chars[i]
        ptr.eow = True
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ptr = self.ptr
        for char in word:
            i = ord(char) - ord('a')
            if not ptr.chars[i]:
                return False
            ptr = ptr.chars[i]
        return ptr.eow

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ptr = self.ptr
        for char in prefix:
            i = ord(char) - ord('a')
            if not ptr.chars[i]:
                return False
            ptr = ptr.chars[i]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
