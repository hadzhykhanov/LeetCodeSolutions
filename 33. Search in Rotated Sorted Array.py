class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        first_item = nums[0]

        while left <= right:
            if target >= first_item:
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle

                elif nums[middle] > target:
                    right = middle - 1

                else:
                    if nums[middle] < first_item:
                        right = middle - 1

                    else:
                        left = middle + 1

            else:
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle

                elif nums[middle] > target:
                    if nums[middle] >= first_item:
                        left = middle + 1
                    else:
                        right = middle - 1

                else:
                    left = middle + 1

        return -1
    