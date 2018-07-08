# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        sol = []
        if not root:
            return sol
        queue = []              # queue to store the "to-be visited" nodes in level order
        current_index = 0       # Index to maintain the start of current level
        next_index = 1          # Index to maintain the start of next level
        queue.append(root)

        while (next_index - current_index != 0):
            intermediate_sol = []
            tmp = next_index
            for i in range(current_index, next_index):
                if not queue[i]:
                    continue
                
                if queue[i].left != None:
                    queue.append(queue[i].left)
                    tmp += 1

                if queue[i].right != None:
                    queue.append(queue[i].right)
                    tmp += 1    
                intermediate_sol.append(queue[i].val)
                
            current_index = next_index
            next_index = tmp
            sol.append(intermediate_sol)
            
        sol.reverse()
        return sol
        
