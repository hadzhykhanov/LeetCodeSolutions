from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memory = defaultdict(int)
        left, res = 0, 0

        for right, cur_char in enumerate(nums):
            memory[cur_char] += 1

            if right - left > k:
                left_item = nums[left]

                memory[left_item] -= 1
                if memory[left_item] == 0: memory.pop(left_item)

                left += 1

            if memory[cur_char] == 2:
                return True

        return False
