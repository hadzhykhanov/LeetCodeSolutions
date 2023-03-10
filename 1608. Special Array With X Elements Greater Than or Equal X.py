class Solution:
    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                if middle == 0 or nums[middle - 1] != target:
                    return middle

                right = middle - 1

            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return left

    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        for x in range(1, len(nums) + 1):
            binary_search_res = self.binary_search(nums, x)
            if len(nums) - binary_search_res == x:
                return x

        return -1


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        first, second = 0, 0

        while first < len(nums) and second < len(nums):
            cur_idx = first + 1

            if cur_idx <= nums[second]:
                if len(nums) - second == cur_idx:
                    return cur_idx
                first += 1

            else:
                second += 1

        return -1
