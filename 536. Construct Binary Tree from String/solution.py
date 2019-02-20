# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s: 'str') -> 'TreeNode':
        # edge cases
        if not s:
            return None
        
        # vars
        left = 1
        right = 2
        done = 3
        stack = []
        
        # loop over the string
        i = 0
        while i < len(s):
            # start of nums
            if s[i] == "(":
                pass
            
            # pop and attach
            elif s[i] == ")":
                child, _ = stack.pop()
                parent, status = stack.pop()
                if status == left:
                    parent.left = child
                    stack.append((parent, right))
                else:
                    parent.right = child
                    stack.append((parent, done))
                    
            # create a node
            else:
                num = [s[i]]
                while i + 1 < len(s) and s[i+1] not in "()":
                    i += 1
                    num.append(s[i])
                    
                node = TreeNode("".join(num))
                stack.append((node, left))
            i += 1
            
        return stack[0][0]
