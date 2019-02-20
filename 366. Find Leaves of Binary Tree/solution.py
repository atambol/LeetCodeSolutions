# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: 'TreeNode') -> 'List[List[int]]':
        # create a map from child to parent
        map = {root: None}
        node = root
        stack = []
        leaves = []
        while node or stack:
            if node:
                if node.left:
                    map[node.left] = node
                if node.right:
                    map[node.right] = node
                    
                if not node.left and not node.right:
                    leaves.append(node)
                    
                stack.append(node.right)
                node = node.left
            else:
                while stack and not node:
                    node = stack.pop()
                    
        # extract leaves
        sol = []
        while leaves:
            s = []
            newleaves = []
            for leaf in leaves:
                # add leaf to s
                s.append(leaf.val)
                
                # update parent
                parent = map[leaf]
                if parent:
                    if parent.left and parent.left == leaf:
                        parent.left = None
                    elif parent.right and parent.right == leaf:
                        parent.right = None

                    # check if parent is a leaf
                    if not parent.left and not parent.right:
                        newleaves.append(parent)
                    
            leaves = newleaves
            sol.append(s)
        return sol
            
                    
