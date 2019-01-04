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
        # serialization converts the tree into preorder traversal
        # the tree is always considered full
        # if a node has any child as null, that child is replaced with a #
        # this way the deserialization can happen with just one traversal
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

        # print("/".join(preorder))
        return "/".join(preorder)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        left = 0
        right = 1
        
        if not data:
            return None
        
        preorder = data.split("/")
        preorder.reverse()
        stack = []
        root = None
        while preorder:
            # extract a value and create a node
            val = preorder.pop()
            if val == "#":
                node = None
            else:
                node = TreeNode(val)
                
            # attach it to the left or right of parent
            if stack:
                parent, side = stack.pop()
                if side == left:
                    parent.left = node
                    stack.append((parent, right))
                else:
                    parent.right = node
            else:
                root = node
            
            # save the node into stack
            if node:
                stack.append((node, left))
                    
        return root
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
