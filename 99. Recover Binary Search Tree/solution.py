# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = list()
        self.inorder(root, None, nodes)
        if nodes:
            nodes[0].val, nodes[1].val = nodes[1].val, nodes[0].val
            
    def inorder(self, root, prev, nodes):
        if not root:
            return prev
        
        prev = self.inorder(root.left, prev, nodes)
        if prev and prev.val > root.val:
            if not nodes:
                nodes.append(prev)
                nodes.append(root)
            else:
                nodes.pop()
                nodes.append(root)
                
        return self.inorder(root.right, root, nodes)
