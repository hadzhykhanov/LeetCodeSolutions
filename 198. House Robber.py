class Solution:
    def rob(self, nums: List[int]) -> int:
        curr_max = nums[0]

        for i in range(2, len(nums)):
            nums[i] = curr_max + nums[i]

            curr_max = max(curr_max, nums[i - 1])

        return max(curr_max, nums[-1])


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        left_max = nums[0]
        cur_max = 0
        cur_max_prev = nums[1]

        for i in range(2, len(nums)):
            cur_max = nums[i] + left_max
            left_max = max(left_max, cur_max_prev)
            cur_max_prev = cur_max

        return max(cur_max, left_max)

