# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # edge cases
        if not l1:
            return l2
        if not l2:
            return l1
        
        # create a dummy head
        head = ListNode(None)
        node = head

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
                
        if l2:
            node.next = l2
        elif l1:
            node.next = l1
            
        return head.next
