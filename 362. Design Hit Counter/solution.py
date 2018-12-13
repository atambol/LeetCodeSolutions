class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # store hits of only 300 recent timestamps - scalable solution O(1) space
        self.hits = [0]*300
        
        # store the previously stabilized timestamp
        self.prev = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        # update the hits counter
        self.stabilize(timestamp)
        key = timestamp%300
        
        # check if it is a new timestamp
        if self.prev == timestamp:
            self.hits[key] += 1
        else:
            self.hits[key] = 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        # update the hits counter
        self.stabilize(timestamp)
        
        # total hits are the sum of all individual hits
        return sum(self.hits)

    def stabilize(self, timestamp):
        # if hits for the same time stamp, no need to stabilize
        if timestamp == self.prev:
            return
        
        # if prev timestamp was longer than 5 minutes ago, reset
        if timestamp - self.prev >= 300:
            self.hits = [0]*300
        else:
            # based on prev and current key, reset only some indices
            key = timestamp%300
            prevKey = self.prev%300
            
            if prevKey < key:
                for i in range(prevKey+1, key+1):
                    self.hits[i] = 0
            else:
                # rollover
                for i in range(prevKey+1, 300):
                    self.hits[i] = 0
                for i in range(0, key+1):
                    self.hits[i] = 0
                    
        self.prev = timestamp

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
