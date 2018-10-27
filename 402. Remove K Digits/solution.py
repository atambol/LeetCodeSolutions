class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # Handle the edge cases
        if len(num) == k:
            return "0"
        
        if len(num) - num.count("0") <= k:
            return "0"
        
        # Remove the first number from left until the order is increasing
        for K in range(k):
            maxi = len(num) - 1
            for i in range(1, len(num)):
                if num[i-1] > num[i]:
                    maxi = i-1
                    print(maxi)
                    break
            
            num = num[:maxi] + num[maxi+1:]    
                
        # remove leading zeroes if any
        return num.lstrip("0")
