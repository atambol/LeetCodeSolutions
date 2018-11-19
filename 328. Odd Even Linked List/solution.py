# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # handle edge cases
        if not head or not head.next:
            return head
        
        # Weave out the even and odd positioned nodes into two separate lists
        odd = ListNode(None)
        oddNode = odd
        even = ListNode(None)
        evenNode = even
        node = head
        flag = True
        
        while node:
            if flag:
                oddNode.next = node
                node = node.next
                oddNode = oddNode.next
                oddNode.next = None
                flag = False
            else:
                evenNode.next = node
                node = node.next
                evenNode = evenNode.next
                evenNode.next = None
                flag = True
    
        # Join the ends and return head
        oddNode.next = even.next            
        return odd.next
                
        
