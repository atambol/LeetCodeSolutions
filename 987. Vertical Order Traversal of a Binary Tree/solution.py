# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.map = collections.defaultdict(list)
    
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        # edge cases
        sol = []
        if not root:
            return sol
        
        # BFS
        queue = [(root, 0)]
        while queue:
            newqueue = []
            for node, pos in queue:
                self.map[pos].append(node.val)
                if node.left:
                    newqueue.append((node.left, pos-1))
                if node.right:
                    newqueue.append((node.right, pos+1))
            
            newqueue.sort(key=lambda x: x[0].val)
            queue = newqueue
            
        # collect solution
        keys = sorted(self.map.keys())
        for k in keys:
            sol.append(self.map[k])
            
        return sol
        
