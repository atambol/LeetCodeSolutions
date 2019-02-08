# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: 'TreeNode', target: 'float', k: 'int') -> 'List[int]':
        if not k or not root:
            return []

        deq = collections.deque()
        self.kSelect(deq, root, target, k)
        return list(deq)
    
    def kSelect(self, deq, root, target, k):
        if not root:
            return
        
        self.kSelect(deq, root.left, target, k)
        
        if len(deq) == k:
            if abs(target - root.val) < abs(deq[0] - target):
                deq.popleft()
                deq.append(root.val)
        else:
            deq.append(root.val)
            
        self.kSelect(deq, root.right, target, k)
        
