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
        This solution combines all the list vals into a single list and uses a heapsort. 
        It then construct new nodes for each of the vals.
        '''
        # Extract vals into heap
        heap = []
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        
        # Construct a new linked list with the vals form heap
        head = ListNode(None)
        node = head
        while heap :
            val = heapq.heappop(heap)
            node.next = ListNode(val)
            node = node.next
            
        return head.next
        
