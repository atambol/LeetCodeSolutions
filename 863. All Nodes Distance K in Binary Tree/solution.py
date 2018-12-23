# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # dfs to construct a graph from the tree
        graph = collections.defaultdict(list)
        stack = []
        node = root
        while node or stack:
            if node:
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)       
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
            
        # bfs from target node to other nodes in graph
        queue = [target.val]
        visited = set()
        while queue and K:
            newqueue = []
            for node in queue:
                for neigbour in graph[node]:
                    if neigbour not in visited:
                        newqueue.append(neigbour)
                visited.add(node)
            queue = newqueue
            K -= 1
            
        return queue
