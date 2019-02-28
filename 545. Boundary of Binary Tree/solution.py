# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        sol = []
        if not root:
            return sol

        sol.append(root.val)

        # left
        left = []
        if root.left:
            node = root.left
            while node:
                left.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right

            left.pop()
        sol.extend(left)

        # bottom
        stack = [root.right]
        node = root.left
        while node or stack:
            if node:
                if not node.left and not node.right:
                    sol.append(node.val)
                    node = None
                else:
                    stack.append(node.right)
                    node = node.left
            else:
                node = stack.pop()

        # right
        right = []
        if root.right:
            node = root.right
            while node:
                right.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left

            right.pop()
            right.reverse()

        sol.extend(right)

        return sol
