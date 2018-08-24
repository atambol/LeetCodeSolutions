# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(None)
        
        res = head
        l = len(lists)
        while True:
            smallest_i = None
            for i in range(l):
                if lists[i]:
                    if smallest_i != None:
                        if lists[smallest_i].val > lists[i].val:
                            smallest_i = i
                    else:
                        smallest_i = i
      
            if smallest_i == None:
                break
            else:
                res.next = lists[smallest_i]
                lists[smallest_i] = lists[smallest_i].next
                res = res.next
                res.next = None
            
        return head.next

        
