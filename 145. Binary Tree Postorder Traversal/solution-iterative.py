# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        postorder = []
        if not root:
            return postorder
        
        node = root
        stack = []
        left = 1
        right = 2
        while node or stack:
            if node:
                stack.append((node, left))
                node = node.left
            else:
                node, status = stack.pop()
                if status == left:
                    stack.append((node, right))
                    node = node.right
                else:
                    postorder.append(node.val)
                    node = None
        
        return postorder
