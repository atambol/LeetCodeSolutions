class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0, 1, 1]
        if num < 3:
            return dp[:num+1]
        power = 2
        for i in range(3, num + 1):
            if i == power*2:
                dp.append(1)
                power = i
            else:
                dp.append(dp[power] + dp[i-power])
                
        return dp
