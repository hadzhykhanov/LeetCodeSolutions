class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                start = middle + 1
            elif nums[middle] > target:
                end = middle - 1

        return -1