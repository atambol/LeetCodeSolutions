class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        size = 0
        if not tree:
            return size
        
        seen = set()
        count = 0
        prev = None
        pcount = 0
        for fruit in tree:
            if fruit in seen:
                if fruit == prev:
                    pcount += 1
                else:
                    pcount = 1
                    prev = fruit
            else:
                if len(seen) == 2:
                    count = pcount
                    for f in seen:
                        if f != prev:
                            seen.remove(f)
                            break
                seen.add(fruit)
                prev = fruit
                pcount = 1
            count += 1
            size = max(size, count)
        return max(size, count)
                
                
