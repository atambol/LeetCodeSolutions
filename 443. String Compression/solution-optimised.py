class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # edge case
        if len(chars) < 2:
            return len(chars)
        
        # O(1) space complexity
        # O(n) time complexity
        i = 0
        j = 0
        count = 0
        while i < len(chars):
            if not i:
                count = 1
            elif chars[i] == chars[i-1]:
                count += 1
            else:
                chars[j] = chars[i-1]
                j += 1
                if count > 1:
                    for c in str(count):
                        chars[j] = c
                        j += 1
                count = 1
            i += 1
            
        # final char
        chars[j] = chars[i-1]
        j += 1
        if count > 1:
            for c in str(count):
                chars[j] = c
                j += 1
        
        # remove excess characters
        while len(chars) > j:
            chars.pop()
        
        return len(chars)
