class Solution:
    @staticmethod
    def first_rob(nums):
        cur_max = nums[0]

        for i in range(2, len(nums)):
            nums[i] += cur_max
            cur_max = max(cur_max, nums[i - 1])

        return max(cur_max, nums[-1])

    def rob(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        return max(self.first_rob(nums[:-1]), self.first_rob(nums[1:]))
