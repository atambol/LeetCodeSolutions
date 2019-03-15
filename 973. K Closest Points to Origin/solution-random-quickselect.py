class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # calculate distance - O(n) time and O(n) space
        arr = []
        for x, y in points:
            d = x*x + y*y
            arr.append((d, (x, y)))

        # use quickselect with random pivot selection - O(n)
        self.quickselect(arr, 0, len(arr)-1, K)
        return [p for d, p in arr[:K]]

    def quickselect(self, arr, low, high, k):
        if low == high:
            return 

        pivot = random.randint(low, high)
        arr[pivot], arr[low] = arr[low], arr[pivot]
        tmp = arr[low]
        pivot = low

        # sort around pivot
        for i in range(low, high+1):
            if arr[i][0] < tmp[0]:
                arr[pivot], arr[i], pivot = arr[i], arr[pivot+1], pivot + 1

        arr[pivot] = tmp
        if pivot == k:
            return
        elif pivot < k:
            self.quickselect(arr, pivot+1, high, k)
        else:
            self.quickselect(arr, low, pivot-1, k)
