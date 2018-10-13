class Solution:
    def __init__(self):
        self.q = []

    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        maxSize = 0
        curSize = 0
        lastCount = 0
        for i, v in enumerate(tree):
            # print(self.q, curSize)
            if v in self.q:
                curSize += 1
                
                # Update the count of last element
                if v == self.q[-1]:
                    lastCount += 1
                else:
                    self.insert(v)
                    lastCount = 1
            else:
                if curSize > maxSize:
                    maxSize = curSize
                if len(self.q) == 0:
                    curSize = 1
                elif len(self.q) == 1:
                    curSize += 1
                else:
                    curSize = 1 + lastCount
                self.insert(v)
                lastCount = 1
        # print(self.q, curSize)
        return max(maxSize, curSize)

    def insert(self, e):
        if len(self.q) == 2:
            self.q.pop(0)
        self.q.append(e)

    
        
