# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # edge case
        if not root:
            return root
        
        # attach a dummy root
        dummy = TreeNode(sys.maxsize)
        dummy.left = root
        prev = dummy
        
        # find the node
        node = root

        while node and node.val != key:
            prev = node
            if node.val < key:
                node = node.right
            elif node.val > key:
                node = node.left

        # check if found
        if not node:
            return root
        
        # adjust subtrees
        left = node.left
        right = node.right
        subtree = None
        if right:
            subtree = right
            if left:
                ptr = right
                while ptr.left:
                    ptr = ptr.left
                ptr.left = left
        else:
            subtree = left
            
        # remove the node
        if prev.left == node:
            prev.left = subtree
        else:
            prev.right = subtree
            
        return dummy.left
                
            
        
