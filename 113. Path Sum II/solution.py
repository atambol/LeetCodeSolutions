# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            paths = self.myPathSum(root, sum)
            for path in paths:
                path.reverse()
            return paths
        
    def myPathSum(self, root, total):
        if not root:                                        # Empty node
            return []
        elif root.left == None and root.right == None:      # Leaf node
            if total == root.val:
                return [[root.val]]
            else:
                return []
        else:                                               # Internal node
            total = total - root.val
            left = self.myPathSum(root.left, total)
            right = self.myPathSum(root.right, total)
            if left and right:
                left = self.appendVal(left, root.val)
                right = self.appendVal(right, root.val)
                return left + right
            elif left:
                left = self.appendVal(left, root.val)
                return left
            elif right:
                right = self.appendVal(right, root.val)
                return right
            else:
                return []
            
    def appendVal(self, arr, val):
        for a in arr:
            a.append(val)
        return arr
                
