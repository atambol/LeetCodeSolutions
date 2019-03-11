class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        state = [0]*length
        ops = [0]*(length+1)
        
        # gather operations
        for x, y, z in updates:
            ops[x] += z
            ops[y+1] -= z
                
        # perform running sum
        total = 0
        for i in range(length):
            total += ops[i]
            state[i] = total
            
        return state
