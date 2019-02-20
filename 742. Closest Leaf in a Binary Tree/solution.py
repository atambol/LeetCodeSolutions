# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root: 'TreeNode', k: 'int') -> 'int':
        # edge cases
        if not root.left and not root.right:
            return root.val
        
        # convert the tree to graph
        # Two edge cases - 
        # 1) root with only one subtree: handled by adding a None element to its neighbours
        # 2) leaf node == k: catch early when creating graph
        graph = {root.val: set([None])} # 1
        stack = []
        node = root
        while node or stack:
            if node:
                if node.val == k and not node.left and not node.right: # 2
                    return node.val
                
                if node.left:
                    graph[node.val].add(node.left.val)
                    graph[node.left.val] = set([node.val])
                if node.right:
                    graph[node.val].add(node.right.val)
                    graph[node.right.val] = set([node.val])
                    
                stack.append(node.right)
                node = node.left
            else:
                while stack and not node:
                    node = stack.pop()

        # bfs until a node is found with no neighbours other than parent
        queue = [k]
        while queue:
            newqueue = []
            for node in queue:
                if not graph[node]:
                    return node
                else:
                    for neigh in graph[node]:
                        if neigh != None:   # handled due to #1
                            graph[neigh].remove(node)
                            newqueue.append(neigh)
                        
            queue = newqueue
        
        
                    
