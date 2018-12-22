# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        leaves = []
        # edge case
        if not root:
            return leaves
        
        # add root
        leaves.append(root.val)
        
        # add left edges
        self.leftLeaves(root.left, leaves)
        
        # add bottom leaves
        self.bottomLeaves(root, leaves)
        
        # add right edges
        self.rightLeaves(root.right, leaves)
        return leaves
    
    def leftLeaves(self, root, leaves):
        node = root
        lleaves = []
        
        # iterative traversal
        while node:
            lleaves.append(node.val)            
            if node.left:
                node = node.left
            else:
                node = node.right
        
        # remove one node that repeats with bottom leaves at the end
        if len(lleaves) > 1:
            leaves.extend(lleaves[:-1])
            
    def bottomLeaves(self, root, leaves):
        stack = [root.right]
        node = root.left
        
        # iterative traversal
        while node or stack:
            if node:
                if not node.left and not node.right:
                    leaves.append(node.val)
                    node = node.left
                else:
                    stack.append(node.right)
                    node = node.left
            else:
                node = stack.pop()
    
    def rightLeaves(self, root, leaves):
        node = root
        rleaves = []
        # iterative traversal
        while node:
            rleaves.append(node.val)            
            if node.right:
                node = node.right
            else:
                node = node.left  
                
        # remove the final node on right edge that repeats in bottom leaves
        rleaves = rleaves[:-1]
        
        # reverse and extend
        leaves.extend(rleaves[::-1])
            
