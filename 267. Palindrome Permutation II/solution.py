class Solution:
    def __init__(self):
        # final solution - set used to prevent repetition
        self.sol = set()
        
    def generatePalindromes(self, s: 'str') -> 'List[str]':
        # get the frequency of all the characters
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
                
        # find out the characters with odd frequency
        singles = 0
        single_c = None
        for k, v in freq.items():
            if v % 2 == 1:
                single_c = k
                singles += 1
                
            # palindrome not possible if more than one odd frequencied characters
            if singles > 1:
                return []
        
        # define the starting point of the permutation
        basestring = collections.deque()
        
        # add the only odd frequencied character and update its frequency
        if single_c:
            basestring.append(single_c)
            freq[single_c] -= 1
            
        # backtrack
        self.backtrack(basestring, freq)
        return list(self.sol)

    def backtrack(self, basestring, freq):
        # get all characters with non zero freq
        chars = list(k for k,v in freq.items() if v > 0)
        
        # if no characters found, a permutation is generated
        if not chars:
            self.sol.add("".join(basestring))
        else:
            # permute for every character
            for c in chars:
                freq[c] -= 2
                basestring.append(c)
                basestring.appendleft(c)
                self.backtrack(basestring, freq)
                basestring.pop()
                basestring.popleft()
                freq[c] += 2
        
                
