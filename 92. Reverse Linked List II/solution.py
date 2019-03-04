# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # edge case
        if m == n:
            return head
    
        # insert dummy head
        node = ListNode(None)
        node.next = head
        head = node
        node = head.next
        prev = head
        
        # reach the mth position
        while m-1:
            prev = node
            node = node.next
            m -= 1
            n -= 1
        
        tail1 = prev
        tail1.next = None
        head2 = node
        prev = None
        
        # reach the nth position
        while n:
            prev = node
            node = node.next
            n -= 1
            
        tail2 = prev
        tail2.next = None
        head3 = node
        
        # reverse between head2 and tail2
        node = head2
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
            
        # attach the lists
        tail1.next = tail2
        head2.next = head3
        
        return head.next
