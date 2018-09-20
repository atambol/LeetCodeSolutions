class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        mask = 1
        solution = 0
        for i in range(32):
            lastBit = n & mask
            n = n >> 1
            
            solution += lastBit << (31-i)
            
        return solution
