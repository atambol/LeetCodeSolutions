# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # insert dummy root
        dummy = TreeNode(sys.maxsize)
        dummy.left = root
        root = dummy
        
        # find the node
        node = root.left
        prev = root
        while node and node.val != key:
            prev = node
            if node.val < key:
                node = node.right
            else:
                node = node.left
        
        if not node:
            return root.left
        
        # remove the node
        child = None
        if node.left and node.right:
            left = node.left
            node2 = node.right
            while node2.left:
                node2 = node2.left
            node2.left = left
            child = node.right
        elif node.left and not node.right:
            child = node.left
        else:
            child = node.right
            
        # attach the child to prev
        if prev.left == node:
            prev.left = child
        else:
            prev.right = child
            
        return root.left
