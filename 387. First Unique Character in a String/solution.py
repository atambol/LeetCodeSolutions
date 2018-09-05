class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        memory = set()
        for i, letter in enumerate(s):
            if letter not in memory:
                pos = s.find(letter, i+1)
                if pos == -1:
                    return i
                else:
                    memory.add(letter)
        return -1
                

        # this should have been faster since it is O(n)
#         memory = {}
#         for letter in s:
#             if letter in memory.keys():
#                 memory[letter] += 1
#             else:
#                 memory[letter] = 1
            
#         for i, letter in enumerate(s):
#             if memory[letter] == 1:
#                 return i
        
#         return -1
