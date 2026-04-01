class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:      
        size = len(nums)

        if size == 0:
            return False

        count = 0
        
        for i in range(len(nums)):
            if nums[i] == target:
                count +=1 
        return count > size / 2 



        