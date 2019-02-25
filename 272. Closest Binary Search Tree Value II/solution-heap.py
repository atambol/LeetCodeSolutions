# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        heap = []
        stack = []
        node = root
        while stack or node:
            if node:
                if len(heap) < k:
                    heapq.heappush(heap, (-abs(target-node.val), node.val))
                else:
                    if -heap[0][0] > abs(node.val - target):
                        heapq.heappushpop(heap, (-abs(target-node.val), node.val))
                        
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
        
        sol = []
        for tup in heap:
            sol.append(tup[1])
            
        return sol
