# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack):
            return True
        else:
            return False
        

    def next(self):
        """
        :rtype: int
        """
        res = self.stack.pop()
        node = res.right
        while node:
            self.stack.append(node)
            node = node.left
        return res.val
            

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
