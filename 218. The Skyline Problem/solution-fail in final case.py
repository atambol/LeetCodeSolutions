class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        sol = []
        if not buildings:
            return sol
        buildings.sort(key = lambda x: (x[0], x[1], x[2]))
        # merge consecutive buildings with same height
        newbuildings = [buildings[0]]
        for b in buildings[1:]:
            if b[2] == newbuildings[-1][2] and b[0] == newbuildings[-1][1]:
                newbuildings[-1][1] = b[1]
            else:
                newbuildings.append(b)
        buildings = newbuildings
        
        end = 1
        start = 0
        B = []
        for b in buildings:
            B.append([b[0], b[2], start])
            B.append([b[1], b[2], end])

        B.sort(key = lambda x: (x[0], x[1]))

        heights = [0] # heap to store height
        sol.append([0,0])
        for b in B:
            if b[2] == start:
                if b[1] > -heights[0]:
                    sol.append([b[0], b[1]])
                heapq.heappush(heights, -b[1])
            else:
                if -heights[0] == b[1]:
                    heapq.heappop(heights)
                    sol.append([b[0], -heights[0]])
                else:
                    i = 0
                    while i < len(heights):
                        if -heights[i] == b[1]:
                            break
                        i += 1
                    heights[i], heights[-1] = heights[-1], heights[i]
                    heights.pop()
                    heapq.heapify(heights)
                    
            if sol[-1][0] == sol[-2][0]:
                keep = sol.pop()
                sol.pop()
                sol.append(keep)
        return sol
            
