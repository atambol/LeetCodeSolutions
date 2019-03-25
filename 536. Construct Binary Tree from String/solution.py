# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None
        
        stack = []
        i = 0
        num = []
        while i < len(s):
            if s[i] == ")":
                node = stack.pop()
                parent = stack.pop()
                if parent.left:
                    parent.right = node
                else:
                    parent.left = node
                stack.append(parent)
                i += 1
            elif s[i] == "(":
                i += 1
            else:
                while i < len(s) and s[i] not in "()":
                    num.append(s[i])
                    i += 1
                val = int("".join(num))
                node = TreeNode(val)    
                stack.append(node)
                num = []
                
        return stack.pop()
