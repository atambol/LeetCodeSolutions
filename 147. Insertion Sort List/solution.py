# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return head
        
        # create a dummy head and tail
        tmp = head
        head = ListNode(-sys.maxsize-1)
        tail = ListNode(sys.maxsize)
        head.next = tail
        tail.next = tmp
        
        while tail.next:
            # extract node
            tmp = tail.next
            tail.next = tmp.next
            tmp.next = None
            
            # insert node to right position
            node = head
            while node.next.val < tmp.val:
                node = node.next
                
            tmp.next = node.next
            node.next = tmp
            
        # remove dummy tail
        node = head
        while node.next.next:
            node = node.next
        node.next = None
        
        # remove dummy head
        return head.next
            
