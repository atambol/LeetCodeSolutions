class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # maintain two helper arrays
        char_arr = []
        count_arr = []
        for char in chars:
            if char_arr and char_arr[-1] == char:
                    count_arr[-1] += 1
            else:
                char_arr.append(char)
                count_arr.append(1)
        
        # crate compressed array
        sol = []
        for count, char in zip(count_arr, char_arr):
            sol.append(char)
            if count > 1:
                for c in str(count):
                    sol.append(c)
        
        # check if compression useful
        if len(sol) <= len(chars):
            i = 0
            while i < len(sol):
                chars[i] = sol[i]
                i += 1
                
            while len(chars) > i:
                chars.pop()
                
        return len(chars)
