# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        boundary = []
        # edge case
        if not root:
            return boundary
        boundary.append(root.val)
        
        # check left
        left = []
        node = root.left
        while node:
            left.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
                
        if left:
            left.pop()
        boundary.extend(left)
        
        # check bottom
        bottom = []
        stack = [root.right]
        node = root.left
        while node or stack:
            if node:
                if not node.left and not node.right:
                    bottom.append(node.val)
                    node = None
                else:
                    stack.append(node.right)
                    node = node.left
            else:
                node = stack.pop()
                
        boundary.extend(bottom)
        
        # check right
        right = []
        node = root.right
        while node:
            right.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
                
        if right:
            right.pop()
        right.reverse()
        boundary.extend(right)
        
        return boundary
