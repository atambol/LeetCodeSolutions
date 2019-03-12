class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # get freq
        freq = {}
        for word in words:
            try:
                freq[word] += 1
            except KeyError:
                freq[word] = 1
                
        # create a heap
        heap = []
        for w, f in freq.items():
            heapq.heappush(heap, (-f, w))
                
        # extract words
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
            
        return res
