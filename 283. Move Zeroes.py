class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        rewrite_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[rewrite_pos] = nums[i]
                rewrite_pos += 1

        for i in range(rewrite_pos, len(nums)):
            nums[i] = 0


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        rewrite_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[rewrite_pos] = nums[rewrite_pos], nums[i]
                rewrite_pos += 1


