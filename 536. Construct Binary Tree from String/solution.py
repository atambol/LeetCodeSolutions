# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        # edge case
        if not s:
            return None
        
        # extract nodes
        stack = []
        left = 1
        right = 2
        done = 3
        num = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                pass
            elif s[i] == ")":
                node, _ = stack.pop()
                parent, status = stack.pop()
                if status == left:
                    parent.left = node
                    stack.append((parent, right))
                else:
                    parent.right = node
                    stack.append((parent, done))
                    
            else:
                j = i
                while i + 1 < len(s) and s[i + 1] not in "()":
                    i += 1
                val = s[j:i+1]
                node = TreeNode(val)
                stack.append((node, left))
            i += 1
                
        return stack[0][0]
                
                
