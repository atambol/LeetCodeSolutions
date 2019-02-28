# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.nodes = []
        
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(None, root)
        node1 = self.nodes.pop()
        node2 = self.nodes.pop()
        node1.val, node2.val = node2.val, node1.val

        
    def inorder(self, prev, node):
        if not node:
            return prev
        
        prev = self.inorder(prev, node.left)
        if prev and prev.val > node.val:
            if self.nodes:
                self.nodes[1] = node
            else:
                self.nodes.append(prev)
                self.nodes.append(node)
        return self.inorder(node, node.right)
