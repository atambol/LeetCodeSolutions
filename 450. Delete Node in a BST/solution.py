# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # attach a dummy root
        node = TreeNode(sys.maxsize)
        node.left = root
        root = node
        
        # search the target node
        node = root
        left = True
        prev = None
        while node and node.val != key:
            if node.val < key:
                prev = node
                left = False
                node = node.right
            else:
                prev = node
                left = True
                node = node.left
        
        # node not found, return as it is
        if not node:
            return root.left
        
        # remove the node and adjust its subtrees
        # if both subtrees are None
        if not node.left and not node.right:
            if left:
                prev.left = None
            else:
                prev.right = None
        # if left subtree exists
        elif node.left and not node.right:
            if left:
                prev.left = node.left
            else:
                prev.right = node.left
        # if right subtree exists
        elif not node.left and node.right:
            if left:
                prev.left = node.right
            else:
                prev.right = node.right
        # if both exist
        else:
            # replace node by its left child
            if left:
                prev.left = node.left
            else:
                prev.right = node.left
        
            # take the right child and push it to the right most position left child's subtree
            right = node.right
            node = node.left
            while node.right:
                node = node.right
            
            node.right = right
        
        return root.left
        
