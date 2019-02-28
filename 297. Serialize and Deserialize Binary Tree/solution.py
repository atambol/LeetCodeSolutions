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
        if not root:
            return ""
        
        preorder = []
        stack = []
        node = root
        while node or stack:
            if node:
                preorder.append(str(node.val))
                stack.append(node.right)
                node = node.left
            else:
                preorder.append("#")
                node = stack.pop()
                
        return ".".join(preorder)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        preorder = data.split(".")
        preorder.reverse()
        root = TreeNode(int(preorder.pop()))
        left = 1
        right = 2
        stack = [(root, left)]
        while preorder:
            val = preorder.pop()
            if val == "#":
                node, status = stack.pop()
                if status == left:
                    stack.append((node, right))
            else:
                node = TreeNode(int(val))
                parent, status = stack.pop()
                if status == left:
                    parent.left = node
                    stack.append((parent, right))
                else:
                    parent.right = node
                    
                stack.append((node, left))
                
        return root
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
