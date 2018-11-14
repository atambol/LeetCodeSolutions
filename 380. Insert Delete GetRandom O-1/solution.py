import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.list.append(val)
            pos = len(self.list) - 1
            self.dict[val] = pos
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            pos = self.dict[val]
            last = len(self.list) - 1
            self.dict[self.list[last]] = pos
            self.list[pos], self.list[last] = self.list[last], self.list[pos]
            self.list.pop()
            self.dict.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        l = len(self.list)
        pos = random.randrange(0, l)
        return self.list[pos]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
