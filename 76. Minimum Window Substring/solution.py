class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if not s or not t:
            return ""
        
        sol = ""
        seen = {}
        
        # get character count
        chars = set(t)
        req_count = [0]*128
        for u in t:
            i = ord(u)
            req_count[i] += 1
        
        i = 0
        j = 0
        act_count = [0]*128
        while j < len(s):
            # move j
            ind = ord(s[j])
            act_count[ind] += 1 
            
            # move i
            ind = ord(s[i])
            act_count[ind] -= 1
            i += 1
            while self.isValidWindow(req_count, act_count):
                ind = ord(s[i])
                act_count[ind] -= 1
                i += 1
                
            i -= 1
            ind = ord(s[i])
            act_count[ind] += 1
            
            # check if this is a valid window and update sol
            if self.isValidWindow(req_count, act_count):
                if not sol:
                    sol = s[i:j+1]
                else:
                    if len(sol) > j - i + 1:
                        sol = s[i:j+1]
            
            j += 1
        return sol
    
    def isValidWindow(self, required, actual):
        for i in range(128):
            if required[i] > actual[i]:
                return False
        return True
