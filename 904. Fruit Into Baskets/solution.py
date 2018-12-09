class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        # max count of fruits in basket
        maxCount = 0 
        
        # count of fruits of two types in basket
        basketCount = 0
        
        # count of previously seen fruit occurance
        prevCount = 0
        
        # previous fruit
        prev = None
        
        # basket that holds two unique fruits
        basket = set()
        
        for fruit in tree:
            # if the fruit is already in basket then just update prevCount
            if fruit in basket:
                if prev == fruit:
                    prevCount += 1
                else:
                    prevCount = 1
                basketCount += 1
            # the fruit is not in the basket, update the basket
            else:
                if len(basket) < 2:
                    basketCount += 1
                else:
                    if basketCount > maxCount:
                        maxCount = basketCount
                    for b in basket:
                        if b != prev:
                            basket.remove(b)
                            break
                    basketCount = 1 + prevCount
                basket.add(fruit)
                prevCount = 1
            prev = fruit
            
        return max(maxCount, basketCount)
