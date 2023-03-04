class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        memory = [0] * 3

        for num in nums:
            memory[num] += 1

        idx = 0
        for item, count in enumerate(memory):
            for _ in range(count):
                nums[idx] = item
                idx += 1

