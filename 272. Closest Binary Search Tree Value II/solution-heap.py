# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        heap = []
        node = root
        stack = []
        while node or stack:
            if node:
                diff = abs(target-node.val)
                if len(heap) == k:
                    if diff < -heap[0][0]:
                        heapq.heappushpop(heap, (-diff, node.val))
                else:
                    heapq.heappush(heap, (-diff, node.val))
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
                
        return [x[1] for x in heap]
