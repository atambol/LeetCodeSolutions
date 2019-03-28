class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        major = nums[0]
        
        for i in range(1, len(nums)):
            if major == nums[i]:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                major = nums[i+1]
                
        return major
