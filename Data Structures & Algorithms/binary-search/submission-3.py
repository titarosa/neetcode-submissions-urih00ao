class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0 or nums[-1] < target:
            return -1

        start, end = 0, len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid 
        return start if nums[start] == target else -1




  




        