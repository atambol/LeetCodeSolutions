from collections import defaultdict

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        # count the frequency of each word
        freq = defaultdict(lambda: 0)
        for word in words:
            freq[word] += 1
            
        # sort the tuple using the freq first and then the word
        sortFreq = [(w, f) for w, f in freq.items()]
        sortFreq.sort(key=lambda x: (-x[1], x[0]))
        
        # grab the first k words 
        return [w[0] for w in sortFreq[:k]]
