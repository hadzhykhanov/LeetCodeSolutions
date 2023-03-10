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
    