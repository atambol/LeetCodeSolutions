class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sol = ""
        l = len(s)
        # Choose a point in string to expand around and check for palindrome
        # expand around indices
        for i in range(l):
            j = k = i

            while j >= 0 and k < l:
                if s[j] == s[k]:
                    j -= 1
                    k += 1
                else:
                    break
            k -= 1
            j += 1
            if abs(k - j) + 1 > len(sol):
                sol = s[j:k+1]

                
        # expand between indices
        for i in range(l):
            j = i
            k = i + 1
            while j >=0 and k < l:
                if s[j] == s[k]:
                    j -= 1
                    k += 1
                else:
                    break
            k -= 1
            j += 1        
            if k - j + 1 > len(sol):
                sol = s[j:k+1]

                
        return sol
