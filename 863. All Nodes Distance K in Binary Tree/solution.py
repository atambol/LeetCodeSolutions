# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # edge case
        if not K:
            return [target.val]
        
        # convert the tree into a graph
        graph = {}
        stack = []
        node = root
        graph[root.val] = set()
        while stack or node:
            if node:
                if node.left:
                    graph[node.val].add(node.left.val)
                    graph[node.left.val] = set([node.val])
                
                if node.right:
                    graph[node.val].add(node.right.val)
                    graph[node.right.val] = set([node.val])
                    
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
                
        # dfs
        def dfs(graph, node, parent, dist):
            if not dist:
                return [node]
            
            solsubset = []
            for neighbour in graph[node]:
                if neighbour != parent:
                    solsubset.extend(dfs(graph, neighbour, node, dist-1))
                
            return solsubset
        
        # count the distance in dfs and collect nodes
        sol = []
        for neigh in graph[target.val]:
            sol.extend(dfs(graph, neigh, target.val, K-1))
            
        return sol
