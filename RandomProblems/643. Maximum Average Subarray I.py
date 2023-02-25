import math


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """sliding window"""
        cur_sum, left = 0, 0
        out = -math.inf

        for right, cur_num in enumerate(nums):
            cur_sum += cur_num

            if right - left == k:
                cur_sum -= nums[left]
                left += 1

            if right - left + 1 == k and cur_sum > out:
                out = cur_sum

        return out / k


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """cumulative sums"""
        out = -math.inf
        cum_sums = [nums[i] for i in range(len(nums))]

        for i in range(1, len(nums)):
            cum_sums[i] += cum_sums[i - 1]
            if i >= k:
                cum_sums[i] -= nums[i - k]

            if i >= k - 1:
                cur_sum = cum_sums[i]
                if cur_sum > out:
                    out = cur_sum

        return out / k if len(nums) != 1 else nums[0]