# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        
        # find total of the tree at root
        total = self.getTotal(root)
        if total % 2 == 1:
            return False
        
        half = total//2
        
        # check if half sum is found
        equal, total = self.checkEqual(root.right, half)
        if equal:
            return equal
        equal, total = self.checkEqual(root.left, half)
        return equal
        
    def getTotal(self, root):
        if not root:
            return 0
        else:
            return self.getTotal(root.left) + self.getTotal(root.right) + root.val
        
    def checkEqual(self, root, half):
        if not root:
            return False, 0
        
        total = root.val
        equal, total1 = self.checkEqual(root.left, half)
        if equal:
            return equal, None
        equal, total2 = self.checkEqual(root.right, half)
        if equal:
            return equal, None
        
        total += total1 + total2
        return total == half, total
