# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.myRightSideView(root, 0, res)
        return res
        
    def myRightSideView(self, root, depth, response):
        if not root:
            return
        
        if depth == len(response):
            response.append(root.val)
        
        self.myRightSideView(root.right, depth + 1, response)
        self.myRightSideView(root.left, depth + 1, response)
        
