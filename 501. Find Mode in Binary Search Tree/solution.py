# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: 'TreeNode') -> 'List[int]':
        freq = {}
        stack = []
        node = root
        maxfreq = 0
        while node or stack:
            if node:
                if node.val in freq:
                    freq[node.val] += 1
                    maxfreq = max(maxfreq, freq[node.val])
                else:
                    freq[node.val] = 1
                    maxfreq = max(maxfreq, freq[node.val])
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()

        sol = []
        for k, v in freq.items():
            if v == maxfreq:
                sol.append(k)
                
        return sol
