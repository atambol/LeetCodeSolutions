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
        # edge case
        if not root:
            return root
        
        # attach a dummy head
        node = TreeNode(sys.maxsize)
        node.left = root
        root = node
        
        # find the key in the tree
        prev = node
        node = root
        while node and node.val != key:
            prev = node
            if key > node.val:
                node = node.right
            else:
                node = node.left
                
        # node not found
        if not node:
            return root.left

        # remove the node
        target = node
        child = None
        
        # arrange the subtree as a BST
        # both children present
        if node.left and node.right:
            node = node.left
            while node.right:
                node = node.right
            node.right = target.right
            child = target.left
            
        # left child present
        elif node.left and not node.right:
            child = node.left
            
        # right child present
        elif not node.left and node.right:
            child = node.right
            
        # no children
        else:
            pass
        
        # attach the remaining subtree to the parent of target
        if prev.left == target:
            prev.left = child
        else:
            prev.right = child
            
        return root.left
                
