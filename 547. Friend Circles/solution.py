
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        visited = [False]*n
        count = 0
        
        # dfs over a user
        def dfs(friends, user, visited):
            if visited[user]:
                return
            visited[user] = True
            for friend, friendship in enumerate(friends[user]):
                if friendship:
                    dfs(friends, friend, visited)
                    
        # visit every user and mark it's circle
        for user in range(n):
            if not visited[user]:
                count += 1
                dfs(M, user, visited)
                
        return count
            
        
