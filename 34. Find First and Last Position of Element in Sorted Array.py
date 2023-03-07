class Solution:
    def binary_search(self, nums, target, pos="less"):
        # only discrete case
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        if pos == "less":
            return left

        if pos == "more":
            return right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_pos = self.binary_search(nums, target - 0.1, "less")
        right_pos = self.binary_search(nums, target + 0.1, "more")

        if left_pos == len(nums) or nums[left_pos] != target:
            return [-1, -1]

        return [left_pos, right_pos]


class Solution:
    def binary_search(self, nums, target, need_first=True):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                if need_first is True:
                    if middle == 0 or nums[middle - 1] != target:
                        return middle

                    right = middle - 1

                else:

                    if middle == len(nums) - 1 or nums[middle + 1] != target:
                        return middle

                    left = middle + 1

            elif nums[middle] < target:
                left = middle + 1

            else:
                right = middle - 1

        return None

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_position = self.binary_search(nums, target, True)

        if left_position is None:
            return [-1, -1]

        return [left_position, self.binary_search(nums, target, False)]
