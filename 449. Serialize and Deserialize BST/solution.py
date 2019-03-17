# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        preorder = []
        
        # edge case
        if not root:
            return preorder
        
        stack = []
        while root or stack:
            if root:
                preorder.append(str(root.val))
                stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
                
        return "#".join(preorder)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # edge case
        if not data:
            return None
        
        preorder = data.split("#")
        preorder.reverse()
        root = TreeNode(int(preorder.pop()))
        stack = [root]
        while preorder:
            node = TreeNode(int(preorder.pop()))
            parent = stack.pop()
            if parent.val > node.val:
                parent.left = node
                stack.append(parent)
            else:
                while stack and stack[-1].val < node.val:
                    parent = stack.pop()
                    
                parent.right = node
            stack.append(node)
            
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
