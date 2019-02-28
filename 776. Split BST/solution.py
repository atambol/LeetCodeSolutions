# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return None, None
        
        if root.val <= V:
            low, high = self.splitBST(root.right, V)
            root.right = low
            return root, high
        else:
            low, high = self.splitBST(root.left, V)
            root.left = high
            return low, root
