# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.myPath(root)
        
    def myPath(self, root):
        if root:
            if root.left and root.right:
                leftPath = self.myPath(root.left)
                rightPath = self.myPath(root.right)
                paths = leftPath + rightPath
                solution = []
                for path in paths:
                    solution.append(str(root.val) + "->" + path)
            elif root.left:
                leftPath = self.myPath(root.left)
                solution = []
                for path in leftPath:
                    solution.append(str(root.val) + "->" + path)
            elif root.right:
                rightPath = self.myPath(root.right)
                solution = []
                for path in rightPath:
                    solution.append(str(root.val) + "->" + path)
            else:
                solution = [str(root.val)]
            return solution
        else:
            return []
