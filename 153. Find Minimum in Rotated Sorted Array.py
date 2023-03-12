class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        first_item = nums[0]

        if first_item <= nums[-1]:
            return first_item

        while left <= right:
            middle = (left + right) // 2

            if middle != 0 and nums[middle - 1] > nums[middle]:
                return nums[middle]

            elif nums[middle] >= first_item:
                left = middle + 1

            else:
                right = middle - 1


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        first_item = nums[0]

        if first_item <= nums[-1]:
            return first_item

        while left <= right:
            middle = (left + right) // 2

            if middle != len(nums) - 1 and nums[middle] > nums[middle + 1]:
                return nums[middle + 1]

            elif nums[middle] >= first_item:
                left = middle + 1

            else:
                right = middle - 1
