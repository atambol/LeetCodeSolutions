class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        prevFruit = None
        prevCount = 0
        maxCount = 0
        curCount = 0
        basket = set()
        
        # pick a fruit
        for fruit in tree:
            # if it is in basket
            if fruit in basket:
                # update the prevFruit and prevCount
                if prevFruit == fruit:
                    prevCount += 1
                else:
                    prevFruit = fruit
                    prevCount = 1
                curCount += 1
            else:
                # if not update maxCount
                maxCount = max(maxCount, curCount)
                curCount = prevCount + 1
                
                # update the basket
                for somefruit in basket:
                    if somefruit != prevFruit:
                        basket.remove(somefruit)
                        break
                basket.add(fruit)
                prevFruit = fruit
                prevCount = 1
                
        return max(maxCount, curCount)
