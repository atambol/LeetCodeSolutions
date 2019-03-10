# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # attach dummy head
        node = ListNode(None)
        node.next = head
        head = node
        
        # reach mth node
        prev = head
        node = head.next
        while m != 1:
            prev = node
            node = node.next
            m -= 1
            n -= 1
        
        # reverse the nodes
        tail1 = prev
        tail2 = node
        prev = None
        while n:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
            n -= 1
            
        # attach all parts together
        tail1.next = prev
        tail2.next = node
        return head.next
        
