# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ## O(n) time complexity
        ## O(1) space complexity
        
        # edge case
        if not root:
            return False
        
        # get the total sum of values of each node in the tree
        total = self.getTotal(root)
        
        # if the total is odd, the answer is false
        if total%2 != 0:
            return False
        else:
            half = total//2
            
        # recurssively match the weight of a subtree with half the total of the tree
        def recur(node):
            '''
            input: TreeNode
            output: int, bool (subtree total, if the solution was found in any of its subtree)
            '''
            # edge case
            if not node:
                return 0, False
            
            # run on left and right subtree
            left, lbool = recur(node.left)
            right, rbool = recur(node.right)
            
            # compare
            if lbool or rbool:
                return 0, True
            else:
                if (node.left != None and left == half) or (node.right != None and right == half):
                    return 0, True
                else:
                    return left + node.val + right, False

        # run on root
        rval, rbool = recur(root)
        return rbool
        
    def getTotal(self,root):
        if not root:
            return 0
        
        return self.getTotal(root.left) + root.val + self.getTotal(root.right)
    
        
        
