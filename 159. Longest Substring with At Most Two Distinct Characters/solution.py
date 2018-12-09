class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        currLen = 0
        prev = None
        prevLen = 0
        substring = set()
        for char in s:
            if char in substring:
                if prev == char:
                    prevLen += 1
                else:
                    prevLen = 1
                    prev = char
                currLen += 1
            else:
                if len(substring) == 2:
                    maxLen = max(maxLen, currLen)
                    for sub in substring:
                        if sub != prev:
                            substring.remove(sub)
                            break

                currLen = prevLen + 1                    
                prevLen = 1     
                substring.add(char)
                
            prev = char
        return max(maxLen, currLen)
                    
