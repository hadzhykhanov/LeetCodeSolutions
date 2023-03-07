class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # O((m + n) * log(m))
        arr2.sort()

        counter = 0
        for item in arr1:
            left, right = 0, len(arr2) - 1

            while left <= right:
                middle = (left + right) // 2

                if abs(item - arr2[middle]) <= d:
                    break

                elif item > arr2[middle]:
                    left = middle + 1

                else:
                    right = middle - 1
            else:
                counter += 1

        return counter





