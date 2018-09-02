# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while end >= start:
            mid = (start + end)/2
            res = guess(mid)
            if not res:
                return mid
            elif res == 1:
                start = mid + 1
            else:
                end = mid - 1
