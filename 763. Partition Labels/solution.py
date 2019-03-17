class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        sol = []
        n = len(S)
        
        # edge case
        if not n:
            return sol
        
        # gather all intervals for every lowercase letter, O(n)
        pos = [None]*26
        for i in range(n):
            index = ord(S[i]) - ord('a')
            if pos[index]:
                pos[index][1] = i
            else:
                pos[index] = [i, i]
                
        # convert to intervals array, O(1)
        intervals = []
        for p in pos:
            if p:
                intervals.append(p)
                
        # sort intervals and merge overlapping intervals, O(1)
        intervals.sort(key = lambda x: (x[0], x[1]))
        merged = [intervals[0]]
        for i in intervals[1:]:
            if i[0] < merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged.append(i)
                
        # get interval lengths, O(1)
        for i in merged:
            sol.append(i[1] - i[0] + 1)
            
        return sol
            
