# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]   
        """
        # Mainain two stacks - one to hold the node and, the
        # other to store if its right child has been visited or not
        stack = []
        seen = []
        visit = []
        
        node = root
        while node or stack:
            # if the node exists, push it to stack and update it to its left child
            if node:
                stack.append(node)
                seen.append(False)
                node = node.left
            # if not, pop the node stack and the seen stack
            else:
                node = stack.pop()
                rightSeen = seen.pop()
                # if the node's right child was not seen, visit it first
                # push the node back to stack, store that its right subtree has been visited
                # and update the node to its right child                
                if not rightSeen:
                    stack.append(node)
                    seen.append(True)
                    node = node.right
                # if the node's right child was seen, visit the node
                else:
                    visit.append(node.val)
                    node = None
                
        return visit
            
            
