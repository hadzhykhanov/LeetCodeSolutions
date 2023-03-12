class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            middle = (left + right) // 2
            middle_sum = (1 + middle) * middle / 2

            if middle_sum == n:
                return middle
            elif middle_sum < n:
                left = middle + 1
            else:
                right = middle - 1

        return right
    