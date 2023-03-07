class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left, right = 1, num // 2
        while left <= right:
            middle = (left + right) // 2

            guess_squared = middle * middle

            if guess_squared == num:
                return True
            elif guess_squared < num:
                left = middle + 1
            else:
                right = middle - 1
        return False