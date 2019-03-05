class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # edge case
        if not length:
            return []
        
        arr = [0]*length
        delta = [0]*(length+1)
        
        # maintain start and end of inc 
        for start, end, inc in updates:
            delta[start] += inc
            delta[end+1] -= inc
            
        # calculate running sum, O(n)
        total = 0
        for i in range(length):
            total += delta[i]
            arr[i] = total
            
        return arr
        
