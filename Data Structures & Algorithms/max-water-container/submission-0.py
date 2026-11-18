class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights) - 1

        max_area = 0

        while left < right:
            
            width = right - left 
            min_height = min(heights[left], heights[right])
            current_area = width * min_height
            max_area = max(current_area, max_area)

            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1

        return max_area        