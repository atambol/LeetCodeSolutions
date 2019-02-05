# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        seen = set()
        remove = set()
        node = ListNode(None)
        node.next = head
        head = node
        node = node.next
        
        while node:
            if not node.val in remove:                
                if node.val in seen:
                    seen.remove(node.val)
                    remove.add(node.val)
                else:
                    seen.add(node.val)

            node = node.next
            
        prev = head
        node = head.next
        while node:
            if node.val in remove:
                prev.next = node.next
            else:
                prev = node
                
            node = node.next
            
        return head.next
