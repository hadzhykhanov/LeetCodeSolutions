class Solution:
    def findKthPositive(self, nums: list[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            nums_of_missed = nums[middle] - middle - 1

            if nums_of_missed < k:
                left = middle + 1

            elif nums_of_missed >= k:
                if middle == 0:
                    return k

                if nums[middle - 1] - middle < k:
                    return nums[middle] - (nums_of_missed - k + 1)

                right = middle - 1

        return nums[-1] + k - nums_of_missed
