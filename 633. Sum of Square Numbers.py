class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c ** (0.5))

        while left <= right:
            left_squared, right_squared = left ** 2, right ** 2
            squares_sum = left_squared + right_squared

            if c in (left_squared, right_squared, squares_sum):
                return True
            elif squares_sum < c:
                left += 1
            else:
                right -= 1

        return False


class Solution:
    def binary_search(self, left, right, target):
        while left <= right:
            middle = ((left + right) // 2)

            squared_middle = middle ** 2
            if squared_middle == target:
                return True
            elif squared_middle > target:
                right = middle - 1
            else:
                left = middle + 1

        return None

    def judgeSquareSum(self, c: int) -> bool:
        for item in range(0, int(c ** (0.5)) + 1):
            if self.binary_search(0, int(c ** (0.5)), c - item ** 2) is not None:
                return True

        return False
