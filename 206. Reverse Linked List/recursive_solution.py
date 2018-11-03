# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = None
        return self.myRev(head, tail)
    
    def myRev(self, head, tail):
        if not head:
            return tail
        else:
            tmp = head.next
            head.next = tail
            return self.myRev(tmp, head)
            
            
