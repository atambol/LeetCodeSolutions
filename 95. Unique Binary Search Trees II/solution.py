# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        if not n:
            return []
        i = 1
        j = n
        return self.myGenerateTrees(i, j)
    
    def myGenerateTrees(self, i, j):
        sol = []
        if i > j:
            sol.append(None)
            return sol
        if i == j:
            sol.append(TreeNode(i))
            return sol
        for k in range(i, j+1):
            left = self.myGenerateTrees(i, k-1)
            right = self.myGenerateTrees(k+1, j)
            for l in left:
                for r in right:
                    node = TreeNode(k)
                    node.left = l
                    node.right = r
                    sol.append(node)
                    
        return sol
