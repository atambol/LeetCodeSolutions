class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # create a set for O(1) get operation
        words = set(wordDict)
        
        # DP to keep track of indices that have been already explored
        searched = [False]*len(s)
        def search(i):
            # if the i is more than the length of s, then search is successful
            if i >= len(s):
                return True
            # if i is already visited, dont do it again
            elif searched[i]:
                return False
            else:
                # mark i visited
                searched[i] = True
                
                # try out each word that can be formed from this index onwards
                for j in range(i, len(s)):
                    # if the word is valid, perform search on the rest of the substring
                    if s[i:j+1] in words:
                        sol = search(j+1)
                        if sol:
                            return sol
                        
                # if nothing works out, search is unsuccessful
                return False
        return search(0)
