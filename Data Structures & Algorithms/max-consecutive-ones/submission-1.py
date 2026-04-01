class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        max_cons = 0
        current_cons = 0

        for n in nums:
            if n == 1:
                current_cons += 1
                max_cons = max(max_cons, current_cons)
            else:
                current_cons = 0
        return max_cons


        