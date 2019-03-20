# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        rev = {}
        stack = []
        node = root
        rev[root] = None
        leaves = []
        
        # create a reverse lookup
        # get leaf nodes
        while node or stack:
            if node:
                if node.left:
                    rev[node.left] = node
                if node.right:
                    rev[node.right] = node
                if not node.left and not node.right:
                    leaves.append(node)
                    
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
                
        # extract nodes
        sol = []
        while leaves:
            sub = []
            newleaves = []
            for leaf in leaves:
                sub.append(leaf.val)
                parent = rev[leaf]
                if parent:
                    if parent.left == leaf:
                        parent.left = None
                    else:
                        parent.right = None
                        
                    if not parent.left and not parent.right:
                        newleaves.append(parent)
                        
            leaves = newleaves
            sol.append(sub)
            
        return sol
        
                
