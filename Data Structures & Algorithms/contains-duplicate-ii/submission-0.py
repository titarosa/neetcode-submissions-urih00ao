class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        windown = set()
        left = 0

        for right in range(len(nums)):
            if nums[right] in windown:
                return True
            windown.add(nums[right])
            if right - left + 1 > k:
                windown.remove(nums[left])
                left += 1
        return False
                

        
        