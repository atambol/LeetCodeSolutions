# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levelOrder = []
        
        # edge cases
        if not root:
            return levelOrder

        # level order traversal
        queue = [root]
        rev = False
        while queue:
            newqueue = []
            level = []
            for node in queue:
                if node.left:
                    newqueue.append(node.left)
                if node.right:
                    newqueue.append(node.right)
                level.append(node.val)
                    
            if rev:
                level.reverse()
                rev = False
            else:
                rev = True
                
            levelOrder.append(level)    
            queue = newqueue
                
        return levelOrder
