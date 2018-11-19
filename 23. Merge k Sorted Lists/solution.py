# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        '''
        This solution picks the node with least val from the top of each list and appends that to a new list. This solution takes a very long time.
        '''
        head = ListNode(None)
        node = head
        listEmpty = False
        
        while not listEmpty:
            n = -1
            leastVal = sys.maxsize
            
            for i in range(len(lists)):
                if lists[i] and lists[i].val < leastVal:
                    n = i
                    leastVal = lists[i].val
            
            if n == -1:
                listEmpty = True
            else:
                node.next = lists[n]
                lists[n] = lists[n].next
                node = node.next
                node.next = None
                
        return head.next
            
