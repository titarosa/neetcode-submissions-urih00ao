class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) <= 1:
            return False

        seen = set()


        for n in nums:
            if n not in seen:
                 seen.add(n)
            else:
                return True
        return False
  
            

        

         