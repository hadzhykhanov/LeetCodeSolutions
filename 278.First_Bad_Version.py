# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        while start <= end:
            middle = (start + end) // 2
            if isBadVersion(middle):
                if middle == 1 or (not isBadVersion(middle - 1)):
                    return middle
                else:
                    end = middle - 1
            else:
                start = middle + 1
