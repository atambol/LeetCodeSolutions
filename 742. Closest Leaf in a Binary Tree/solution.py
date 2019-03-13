# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        # convert the tree into a graph
        graph = {}
        stack = []
        node = root
        leaves = set()
        while node or stack:
            if node:
                if not node.val in graph:
                    graph[node.val] = set()
                
                is_leaf = True
                if node.left:
                    is_leaf = False
                    graph[node.val].add(node.left.val)
                    graph[node.left.val] = set()
                    graph[node.left.val].add(node.val)
                if node.right:
                    is_leaf = False
                    graph[node.val].add(node.right.val)
                    graph[node.right.val] = set()
                    graph[node.right.val].add(node.val)
                    
                if is_leaf:
                    leaves.add(node.val)
                    
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
                
        # bfs from k
        queue = [k]
        while queue:
            newqueue = set()
            for node in queue:
                if node in leaves:
                    return node
                else:
                    for neigh in graph[node]:
                        graph[neigh].remove(node)
                        newqueue.add(neigh)
            queue = newqueue           
        return

                    
                
