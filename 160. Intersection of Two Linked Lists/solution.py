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
        # Edge cases
        if not headA or not headB:
            return None
        
        # Get list lengths
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        
        # identify lists based on length
        diff = abs(lenA - lenB)
        if (lenA > lenB):
            node1 = headA
            node2 = headB
        else:
            node1 = headB
            node2 = headA
            
        # traverse the larger list until the difference is matched
        while diff:
            diff -= 1
            node1 = node1.next
            
        # traverse both lists to identify coinciding node
        while node1 and node2:
            if node1 == node2:
                return node1
            else:
                node1 = node1.next
                node2 = node2.next
                
        return None
    
    
    def getLength(self, head):
        l = 0
        while (head):
            head = head.next
            l += 1
        return l
