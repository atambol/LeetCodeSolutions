class FreqStack:
    def __init__(self):
        self.heap = []
        self.count = 0
        self.freq = {}
        
    def push(self, x: int) -> None:
        # set the freq
        if x in self.freq:
            self.freq[x] += 1
        else:
            self.freq[x] = 1
            
            
        # insert into heap with the freq and position
        heapq.heappush(self.heap, (-self.freq[x], -self.count, x))
        self.count += 1

    def pop(self) -> int:
        _, _, x = heapq.heappop(self.heap)
        self.freq[x] -= 1
        if not self.freq[x]:
            self.freq.pop(x)
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
