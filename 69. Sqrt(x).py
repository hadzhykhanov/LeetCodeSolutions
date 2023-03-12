class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            middle = (left + right) // 2
            squared_middle = middle * middle

            if squared_middle == x:
                return middle

            elif squared_middle > x:
                right = middle - 1

            else:
                left = middle + 1

        return right
