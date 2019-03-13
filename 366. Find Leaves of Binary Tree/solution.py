# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        # construct a map from child to parent
        parent = {}
        stack = []
        node = root
        leaves = []
        while stack or node:
            if node:
                is_leaf = True
                if node.left:
                    is_leaf = False
                    parent[node.left] = node
                if node.right:
                    is_leaf = False
                    parent[node.right] = node
                if is_leaf:
                    leaves.append(node)
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
                
        # collect leaves and remove
        sol = []
        while leaves:
            s = []
            newleaves = []
            for leaf in leaves:
                s.append(leaf.val)
                if leaf in parent:
                    p = parent[leaf]
                    if p.left == leaf:
                        p.left = None
                    elif p.right == leaf:
                        p.right = None

                    if not p.left and not p.right:
                        newleaves.append(p)

            sol.append(s)
            leaves = newleaves
        
        return sol
