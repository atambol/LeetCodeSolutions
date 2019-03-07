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
        
        # pivot is random element in current window
        pivot = random.randint(low, high)
        arr[low], arr[pivot] = arr[pivot], arr[low]
        x = arr[low]
        pivot = low
        for i in range(low, high+1):
            if arr[i] < x:
                arr[i], arr[pivot], pivot = arr[pivot+1], arr[i], pivot+1
                
        arr[pivot] = x
        if pivot == target:
            return
        elif pivot < target:
            return self.quickselect(arr, pivot + 1, high, target)
        else:
            return self.quickselect(arr, low, pivot - 1, target)
        
