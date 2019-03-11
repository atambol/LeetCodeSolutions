# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        # O(n) time complexity
        deq = collections.deque()
        self.kselect(root, deq, target, k)
        return list(deq)
    
    def kselect(self, root, deq, target, k):
        if not root:
            return deq
        
        self.kselect(root.left, deq, target, k)
        if len(deq) == k:
            if abs(deq[0] - target) > abs(root.val - target):
                deq.popleft()
                deq.append(root.val)
        else:
            deq.append(root.val)
                
        self.kselect(root.right, deq, target, k)
