class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # default case of uglies is 1
        uglies = [1]
        
        # pointers to numbers next in line for multiplication
        i2 = 0
        i3 = 0
        i5 = 0
        
        # until we done find the nth ugly number
        while len(uglies) < n:
            # find out all the candidate uglies
            candidates = [uglies[i2]*2, uglies[i3]*3, uglies[i5]*5]
            
            # get the minimum
            ugly = min(candidates)
            if ugly == candidates[0]:
                i2 += 1
            elif ugly == candidates[1]:
                i3 += 1
            else:
                i5 += 1
                
            # if the ugly is new, add it to the list
            if ugly > uglies[-1]:
                uglies.append(ugly)
            
        return uglies[-1]
