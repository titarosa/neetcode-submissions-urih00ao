class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0 , len(heights) - 1
        maxArea = 0

        while left < right:
            minHeight = min(heights[left], heights[right])
            width = (right - left) 
            area = minHeight * width
            if maxArea < area:
                maxArea = area
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return maxArea

