class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0, 1, 1]
        if num == 0:
            return dp[:1]
        if num == 1:
            return dp[:2]
        if num == 2:
            return dp
        
        i = 2
        prevPow = 2
        while i < num:
            i += 1
            if i == prevPow*2:
                prevPow = i
                dp.append(1)
            else:
                dp.append(dp[prevPow] + dp[i - prevPow])
        return dp
            
        
        
