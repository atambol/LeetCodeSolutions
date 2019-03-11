# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, root: ListNode, k: int) -> ListNode:
        # edge case
        if not root:
            return root
        
        # get the length
        l = 0
        node = root
        while node:
            node = node.next
            l += 1
        i = l//k    
        
        # attach a dummy node
        dummy = ListNode(None)
        dummy.next = root
        tail1 = dummy
        tail2 = root
        node = root
        
        # reverse nodes
        while i:
            prev = None
            for j in range(k):
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            tail1.next = prev
            tail1 = tail2
            tail2 = node
            i -= 1
        # attach final bit
        tail1.next = node
        return dummy.next
            
