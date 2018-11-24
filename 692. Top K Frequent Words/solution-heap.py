class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        # count the frequency of each word
        freq = {}
        for word in words:
            # this is an alternative to default dictionary
            freq[word] = freq.get(word, 0) + 1
            
        # push elements into heap
        heap = []
        for word, count in freq.items():
            # reverse the count using negative sign
            # python heaps are min heaps by default
            # this would push the most freq element to the top
            # also, heap orders the element using both count and word
            # so there is no need to use a key to sort words lexicographically in case of a tie
            heapq.heappush(heap, (-count, word))
            
        # extract the top k words in the heap
        return [ x[1] for x in heapq.nsmallest(k, heap) ]
        
        
            
