# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        p1 = headA
        p2 = headB
        
        pass1A = False
        pass1B = False
        
        while p1 != p2 or not pass1A or not pass1B:
            if not p1:
                if not pass1A:
                    pass1A = True
                    p1 = headB
                else:
                    return None
            else:
                p1 = p1.next
                    
            if not p2:
                if not pass1B:
                    pass1B = True
                    p2 = headA
                else:
                    return None
            else:
                p2 = p2.next
                
        if p1 == p2:
            return p1
        else:
            return None
                
            
