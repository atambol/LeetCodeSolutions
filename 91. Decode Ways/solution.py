class Solution:
    def numDecodings(self, s: str) -> int:
        visited = [0]*len(s)
        return self.backtrack(s, 0, visited)
        
    def backtrack(self, s, low, visited):
        if visited[low]:
            return visited[low]
        
        count = 0
        for i in range(low+1,len(s)+1):
            if 0 < int(s[low:i]) <= 26:
                if i == len(s):
                    count += 1
                else:
                    count += self.backtrack(s, i, visited)
            else:
                break
                
        visited[low] = count
        return count
