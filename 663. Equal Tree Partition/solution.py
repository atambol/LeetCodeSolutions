# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        subtreeSumList = []
        queue = []

        # Calculate the subtree sum with root node
        def subtreeSum(node):
            if not node:
                return 0
            
            if not node.left and not node.right:
                subtreeSumList.append(node.val)
                return node.val
            
            mySubtreeSum = subtreeSum(node.left) + subtreeSum(node.right) + node.val
            subtreeSumList.append(mySubtreeSum)
            
            return mySubtreeSum
        
        # Get the total tree's sum
        treeSum = subtreeSum(root)
        
        # Compare subtree total with tree total
        for subtreeSum in subtreeSumList[:-1]:
            if treeSum == subtreeSum * 2:
                return True
            
        return False
        
        
