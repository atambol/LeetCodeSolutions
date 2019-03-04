# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1 = ListNode(None)
        head2 = ListNode(None)
        
        # two pointer technique
        ptr = head
        ptr1 = head1
        ptr2 = head2
        while ptr:
            if ptr.val < x:
                ptr1.next = ptr
                ptr1 = ptr1.next
                ptr = ptr.next
                ptr1.next = None
            else:
                ptr2.next = ptr
                ptr2 = ptr2.next
                ptr = ptr.next
                ptr2.next = None
                
        # join the lists
        ptr1.next = head2.next
        
        return head1.next
                
