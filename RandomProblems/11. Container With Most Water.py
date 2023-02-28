import math


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = -math.inf
        left, right = 0, len(height) - 1

        while left < right:
            curr_width = right - left
            max_area = max(max_area, curr_width * (min(height[left], height[right])))

            if height[left] >= height[right]:
                right -= 1
            else:
                curr_min = height[left]
                left += 1

        return max_area