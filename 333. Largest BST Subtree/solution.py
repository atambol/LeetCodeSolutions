# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.min = -sys.maxsize-1
        self.max = sys.maxsize
    def largestBSTSubtree(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        
        _, _, count = self.myLargestBSTSubtree(root)
        return count
    
    def myLargestBSTSubtree(self, root):
        if root.right and root.left:
            llow, lhigh, lcount = self.myLargestBSTSubtree(root.left)
            rlow, rhigh, rcount = self.myLargestBSTSubtree(root.right)
            if llow <= lhigh < root.val < rlow <= rhigh:
                return llow, rhigh, lcount + rcount + 1
            else:
                if lcount > rcount:
                    return self.max, self.min, lcount
                else:
                    return self.max, self.min, rcount
        elif not root.right and root.left:
            llow, lhigh, lcount = self.myLargestBSTSubtree(root.left)
            if llow <= lhigh < root.val:
                return llow, root.val, lcount + 1
            else:
                return self.max, self.min, lcount
        elif root.right and not root.left:
            rlow, rhigh, rcount = self.myLargestBSTSubtree(root.right)
            if root.val < rlow <= rhigh:
                return root.val, rhigh, rcount + 1
            else:
                return self.max, self.min, rcount
        else:
            return root.val, root.val, 1
                    
