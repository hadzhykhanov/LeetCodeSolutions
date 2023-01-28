class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i, item in enumerate(nums):
            if left_sum == total_sum - left_sum - item:
                return i
            left_sum += item

        return -1
