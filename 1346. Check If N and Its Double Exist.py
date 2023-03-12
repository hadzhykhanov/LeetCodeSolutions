from collections import defaultdict


class Solution:
    def checkIfExist(self, nums: List[int]) -> bool:
        memory = defaultdict(list)

        for idx, item in enumerate(nums):
            memory[item].append(idx)

        for idx, item in enumerate(nums):
            if item * 2 in memory and (item != 0 or len(memory[item]) >= 2):
                return True

        return False


class Solution:
    def checkIfExist(self, nums: List[int]) -> bool:
        memory = defaultdict(list)

        for idx, item in enumerate(nums):
            memory[item].append(idx)
            if item * 2 in memory or item / 2 in memory:
                if item != 0 or len(memory[item]) >= 2:
                    return True

        return False


class Solution:
    def checkIfExist(self, nums: list[int]) -> bool:
        nums.sort()

        first, second = 0, 0

        while first < len(nums) and second < len(nums):
            doubled_first = nums[first] * 2

            if doubled_first == nums[second]:
                if first != second:
                    return True

                second += 1
            elif doubled_first > nums[second]:
                second += 1

            else:
                first += 1

        return False

