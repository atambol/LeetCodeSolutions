# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen = set()
        stack = []
        node = root
        while node or stack:
            if node:
                if node.val in seen:
                    return True
                seen.add(k-node.val)
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
                
        return False
