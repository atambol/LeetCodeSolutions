"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> 'List[int]':
        node = root
        sol = []
        pos = 0
        if not node:
            return sol
        
        stack = []
        while stack or node:
            # print(node.val)
            if pos == len(node.children):
                sol.append(node.val)
                if stack:
                    node, pos = stack.pop()
                else:
                    node = None
            else:
                stack.append((node, pos+1))
                node = node.children[pos]
                pos = 0
                
        return sol
