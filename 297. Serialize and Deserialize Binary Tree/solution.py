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
        sol = []
        stack = []
        preorder = []
        node = root
        
        # iterative preorder traversal
        while node or stack:
            if node:
                preorder.append(str(node.val))
                stack.append(node.right)
                node = node.left
            else:
                preorder.append("#")
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
        
        # split the serialisation
        preorder = data.split(",")[::-1]
        root = TreeNode(preorder.pop())
        node = root
        stack = [root]
        count = [0]
        
        # loop over preorder to extract values
        # the child count is exactly two in this serialization
        # maintain a count array to keep track of left and right child
        while preorder:
            # if the count of children is two for the last node in stack
            # it is full so pop it
            if count[-1] == 2:
                node = stack.pop()
                count.pop()
            else:
                # extract a new value from preorder
                val = preorder.pop()
                if val != "#":
                    # create a node from val
                    node = TreeNode(val)
                    parent = stack[-1]
                    
                    # if the parent has 0 children, then node is a left child
                    if count[-1] == 0:
                        parent.left = node
                    # if the parent has 1 children, then node is a right child
                    else:
                        parent.right = node
                        
                    # increment the child count of parent
                    count[-1] += 1
                    
                    # append the child node
                    stack.append(node)
                    count.append(0)
                else:
                    # None added as child
                    count[-1] += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
