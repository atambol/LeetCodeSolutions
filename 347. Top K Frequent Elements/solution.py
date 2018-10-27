from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Get the count of numbers
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            
        # Create a list out of it
        arr = []
        for num in counts:
            arr.append([counts[num], num])    
        
        # Heapify and Extract the k largest 
        res = heapq.nlargest(k, arr)
        
        # Return the elements only
        return list(x[1] for x in res)

            
