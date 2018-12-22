# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            queue = [root]
            while queue:
                newqueue = []
                for node in queue:
                    if node.left:
                        newqueue.append(node.left)
                    if node.right:
                        newqueue.append(node.right)

                for i in range(len(queue)-1):
                    queue[i].next = queue[i+1]
                queue[-1].next = None

                queue = newqueue
