# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Split up
        prev = None
        sptr = head
        fptr = head
        while fptr:
            prev = sptr
            sptr = sptr.next
            fptr = fptr.next
            if fptr:
                fptr = fptr.next
                              
        # Reverse head2
        head2 = prev.next
        prev.next = None
        prev = None
        while head2:
            tmp = head2.next
            head2.next = prev
            prev = head2
            head2 = tmp
        head2 = prev        
        
        # Weave in
        node = head
        head1 = head.next
        odd = False
        while head1 or head2:
            if odd:
                node.next = head1
                head1 = head1.next
                node = node.next
                odd = False
            else:
                node.next = head2
                head2 = head2.next
                node = node.next
                odd = True  
