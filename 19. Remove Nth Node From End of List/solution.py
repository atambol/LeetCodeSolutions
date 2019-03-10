# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # attach a dummy node
        node = ListNode(None)
        node.next = head
        head = node
        
        # two runners
        fptr = head.next
        while fptr and n:
            n -= 1
            fptr = fptr.next
            
        sptr = head
        while fptr:
            sptr = sptr.next
            fptr = fptr.next
            
        # remove the node
        sptr.next = sptr.next.next
        return head.next
        
