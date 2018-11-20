# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        visited = []
        stack = []
        node = root
        
        # Use inorder traversal
        while node or stack:
            # break if the kth element is found
            if len(visited) == k:
                break
            if node:
                # check left
                stack.append(node)
                node = node.left
            else:
                # check self
                node = stack.pop()
                visited.append(node.val)
                
                # check right
                node = node.right
        
        return visited[-1]
