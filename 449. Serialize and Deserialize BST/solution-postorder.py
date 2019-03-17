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
        postorder = []
        
        # edge case
        if not root:
            return postorder
        
        stack = []
        left = 1
        right = 2
        while root or stack:
            if root:
                stack.append((root, left))
                root = root.left
            else:
                root, status = stack.pop()
                if status == left:
                    stack.append((root, right))
                    root = root.right
                else:
                    postorder.append(str(root.val))
                    root = None
                
        return "#".join(postorder)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # edge case
        if not data:
            return None
        
        postorder = data.split("#")
        root = TreeNode(int(postorder.pop()))
        stack = [root]
        while postorder:
            node = TreeNode(int(postorder.pop()))
            parent = stack.pop()
            if parent.val < node.val:
                parent.right = node
                stack.append(parent)
            else:
                while stack and stack[-1].val > node.val:
                    parent = stack.pop()
                    
                parent.left = node
            stack.append(node)
            
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
