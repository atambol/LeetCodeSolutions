# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.half = None
        self.equal = False
        
    def checkEqualTree(self, root: TreeNode) -> bool:
        # get the total weight
        total = self.getTotal(root)
                
        # get the half
        if total%2 == 1:
            return False
        
        self.half = total//2
        
        # check if the mid point exists
        self.checkTotal(root)
        
        return self.equal
                
    def getTotal(self, node):
        stack = []
        total = 0
        while stack or node:
            if node:
                total += node.val
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
                
        return total
    
    def checkTotal(self, node):
        if not node:
            return None
        
        totals = []
        if node.left:
            totals.append(self.checkTotal(node.left))
        
        if node.right:
            totals.append(self.checkTotal(node.right))
            
        if self.half in totals:
            self.equal = True
            
        totals.append(node.val)
        return sum(totals)
