# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = []
        
        # if non empty root
        if root:
            queue = [root]
            
            # perform level order traversal
            while queue:
                newqueue = []
                
                # append value of right most node of queue
                view.append(queue[-1].val)
                
                # save the nodes of next level
                for node in queue:
                    if node.left:
                        newqueue.append(node.left)
                    if node.right:
                        newqueue.append(node.right)

                queue = newqueue

        return view
                
        
        
