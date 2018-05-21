import queue

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        q = queue.Queue()
        if x < 0:
            negative = -1
        else:
            negative = 1

        x = abs(x)
        while x != 0:
            q.put(x % 10)
            x //= 10

        ans = 0
        while not q.empty():
            ans = ans*10 + q.get()

        if ans.bit_length() > 31:
            return 0
        else:
            return ans*negative
