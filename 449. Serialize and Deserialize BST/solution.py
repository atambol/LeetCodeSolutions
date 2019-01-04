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
        
        # preorder traversal of tree
        preorder = []
        stack = []
        node = root
        while node or stack:
            if node:
                preorder.append(str(node.val))
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
                
        return "/".join(preorder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        preorder = data.split("/")
        
        # reverse the order to make it easy to pop
        preorder.reverse()
        
        # create root node
        root = TreeNode(int(preorder.pop()))
        stack = [root]
        
        # while there are nodes in traversal
        while preorder:
            # pop a node
            node = TreeNode(int(preorder.pop()))
            
            # pop a parent
            parent = stack.pop()
            
            # if the node's val is less than parent's val, it goes to the left
            if node.val < parent.val:
                parent.left = node
                stack.append(parent)
            else:
                # else it goes to the right
                # the parent is then chosen by popping as many parents from the stack 
                # the parents are popped until they have a value less than that of node
                while stack and stack[-1].val < node.val:
                    parent = stack.pop()
                parent.right = node
                
            # push the node back to the stack
            stack.append(node)
            
        return root
            
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
