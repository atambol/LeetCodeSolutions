class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        uglies = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        
        while len(uglies) != n:
            ugly = min(2*uglies[p2], 3*uglies[p3], 5*uglies[p5])
            if 2*uglies[p2] == ugly:
                p2 += 1
            elif 3*uglies[p3] == ugly:
                p3 += 1
            elif 5*uglies[p5] == ugly:
                p5 += 1
                
            if ugly > uglies[-1]:
                uglies.append(ugly)
                
        return uglies[-1]
