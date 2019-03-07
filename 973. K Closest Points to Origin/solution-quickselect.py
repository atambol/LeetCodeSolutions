class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # calculate the distance of all points from origin
        arr = []
        for x, y in points:
            dist=x*x + y*y
            arr.append((dist, (x,y)))

        # perform quick select on the points
        self.quickselect(arr, 0, len(arr)-1, K)
        return [x[1] for x in arr[:K]]
    
    def quickselect(self, arr, low, high, target):
        if low == high:
            return
        
        # pivot is left most element in current window
        x = arr[low]
        j = low
        for i in range(low, high+1):
            if arr[i] < x:
                arr[i], arr[j], j = arr[j+1], arr[i], j+1
                
        arr[j] = x
        if j == target:
            return
        elif j < target:
            return self.quickselect(arr, j + 1, high, target)
        else:
            return self.quickselect(arr, low, j - 1, target)
        
