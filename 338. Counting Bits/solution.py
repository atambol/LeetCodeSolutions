class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        powOfTwo = 1
        dp = [0, 1]
        for i in range(2, num+1):
            if powOfTwo*2 == i:
                dp.append(1)
                powOfTwo *= 2
            else:
                dp.append(1+dp[i-powOfTwo])
        return dp[:num+1]
