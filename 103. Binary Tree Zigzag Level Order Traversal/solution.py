# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        sol = []
        if not root:
            return sol
        
        queue = []
        current_index = 0
        next_index = 1
        queue.append(root)
        flag = False
        
        while (next_index - current_index != 0):
            intermediate_sol = []
            tmp = next_index
            for i in range(current_index, next_index):
                if not queue[i]:
                    continue
                intermediate_sol.append(queue[i].val)
                if queue[i].left != None:
                    queue.append(queue[i].left)
                    tmp += 1

                if queue[i].right != None:
                    queue.append(queue[i].right)
                    tmp += 1
            current_index = next_index
            next_index = tmp
            if flag:
                intermediate_sol.reverse()
                flag = False
            else:
                flag = True
            print(intermediate_sol)
            sol.append(intermediate_sol)
            
        return sol
