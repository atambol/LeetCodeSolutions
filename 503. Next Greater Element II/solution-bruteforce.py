class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        map = {}
        l = len(nums)
        sol = [None]*l
        for i in range(l-1, -1, -1):
            j = i+1
            sol[i] = -1
            while j%l != i:
                if nums[j%l] > nums[i]:
                    sol[i] = nums[j%l]
                    break
                else:
                    if sol[j%l] and sol[j%l] > nums[i]:
                        sol[i] = sol[j%l]
                        break
                j += 1
        return sol
