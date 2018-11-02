# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        else:
            paths = []
            for path in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right):
                paths.append(str(root.val) + "->" + path)
            if not paths:
                paths.append(str(root.val))
            return paths
            
            
