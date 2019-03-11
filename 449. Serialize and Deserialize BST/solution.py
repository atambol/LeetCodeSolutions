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
        
        postorder = []
        stack = []
        node = root
        left = 1
        right = 2
        while node or stack:
            if node:
                stack.append((node, left))
                node = node.left
            else:
                node, status = stack.pop()
                if status == left:
                    stack.append((node, right))
                    node = node.right
                else:
                    postorder.append(str(node.val))
                    node = None
        return "#".join(postorder)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        postorder = data.split("#")
        root = TreeNode(int(postorder.pop()))
        stack = [root]
        while postorder:
            node = TreeNode(int(postorder.pop()))
            if node.val > stack[-1].val:
                stack[-1].right = node
            else:
                parent = stack.pop()
                while stack and stack[-1].val > node.val:
                    parent = stack.pop()
                    
                parent.left = node
                
            stack.append(node)
            
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
