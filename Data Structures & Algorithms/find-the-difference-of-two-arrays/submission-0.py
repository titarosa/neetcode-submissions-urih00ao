class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diff_1 = set(nums1) - set(nums2)
        diff2 =  set(nums2) - set(nums1)
        return [list(diff_1), list(diff2)]
        
        # time o(n + m) space o(n + m) worse case