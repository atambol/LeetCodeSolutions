class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return list(set(nums))
        
        n1 = None
        n2 = None
        c1 = 0
        c2 = 0
        
        for i in range(len(nums)):
            if n1 == nums[i]:
                c1 += 1
            elif n2 == nums[i]:
                c2 += 1
            elif c1 == 0:
                n1 = nums[i]
                c1 = 1
            elif c2 == 0:
                n2 = nums[i]
                c2 = 1
            else:
                c2 -= 1
                c1 -= 1

        
        sol = set()
        if nums.count(n1) > len(nums)//3:
            sol.add(n1)
        if nums.count(n2) > len(nums)//3:
            sol.add(n2)

        return list(sol)
