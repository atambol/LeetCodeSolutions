class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # count the word frequency
        freq = {}
        for word in words:
            try:
                freq[word] = freq[word] + 1
            except:
                freq[word] = 1
                
        # add the (-freq, word) tuple to a list
        # reverse the frew using negative sign
        # python heaps are min heaps by default
        # this would push the most freq element to the top
        # also, heap orders the element using both count and word
        # so there is no need to use a key to sort words lexicographically in case of a tie
        wordfreq = [(-f, w) for w,f in freq.items()]
        
        # heapify the list
        heapq.heapify(wordfreq)
        
        # select the smallest k elements
        topk = heapq.nsmallest(k, wordfreq)
        
        # return only the words from tuple list
        return [i[1] for i in topk]
