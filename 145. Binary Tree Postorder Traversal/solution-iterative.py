# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        node = root
        postorder = []
        right = 2
        left = 1
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
