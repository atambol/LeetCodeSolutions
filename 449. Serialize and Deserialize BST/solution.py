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
        node = root
        stack = []
        preorder = []
        
        # calculate the preorder traversal of the BST using iterative method
        while node or stack:
            if node:
                preorder.append(str(node.val))
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()

        return ",".join(preorder)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # edge case
        if not data:
            return None
        else:
            # create the preorder list, reverse it to optimise pop operations
            preorder = [ int(x) for x in data.split(",")[::-1]]
            
            # read the list from right to left due to reversal
            # root node is the last element right now
            root = TreeNode(preorder.pop())
            stack = [root]
            # untils there are elements on the preorder list
            while preorder:
                # pop the last element
                node = TreeNode(preorder.pop())
                parent = stack[-1]
                
                # compare it with the parent node
                if parent.val < node.val:
                    # node > parent, find the largest parent in the stack smaller than node
                    while stack and stack[-1].val < node.val:
                        parent = stack.pop()
                    
                    # attach node to the right
                    parent.right = node
                else:
                    # attack node to the left
                    parent.left = node
                    
                # push the node back to the stack
                stack.append(node)
                
            return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
