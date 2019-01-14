# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.node = root

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        while self.stack or self.node:
            if self.node:
                self.stack.append(self.node)
                self.node = self.node.left
            else:
                node = self.stack.pop()
                self.node = node.right
                return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.stack or self.node:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
