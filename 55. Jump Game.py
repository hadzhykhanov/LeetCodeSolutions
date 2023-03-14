class Solution:
    def canJump(self, nums: list[int]) -> bool:
        cur_max, cur_idx = 0, 0

        while cur_idx <= cur_max:
            cur_max = max(cur_max, cur_idx + nums[cur_idx])
            cur_idx += 1

            if cur_max >= len(nums) - 1:
                return True

        return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_max = 0

        for i in range(len(nums)):
            if i > cur_max:
                return False

            cur_max = max(cur_max, i + nums[i])

            if cur_max >= len(nums) - 1:
                return True


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_idx:
                last_idx = i

        return last_idx == 0
