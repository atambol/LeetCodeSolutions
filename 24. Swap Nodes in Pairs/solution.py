# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # weave in and out to extract nodes
        ptr = head
        dummy = ListNode(None)
        prev = dummy
        while ptr and ptr.next:
            tmp = ptr.next.next
            prev.next = ptr.next
            prev.next.next = ptr
            ptr.next = tmp
            prev = ptr
            ptr = tmp
        
        return dummy.next
                
        
