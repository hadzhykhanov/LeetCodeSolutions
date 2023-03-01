class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = dict()
        for ind, item in enumerate(nums):
            memory[item] = ind

        for idx, item in enumerate(nums):
            complement = target - item
            if complement in memory and memory[complement] != idx:
                return [idx, memory[complement]]