class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 2
        while left <= right:
            middle = (left + right) // 2

            if arr[middle - 1] < arr[middle] and arr[middle] > arr[middle + 1]:
                return middle

            elif arr[middle - 1] < arr[middle]:
                left = middle + 1

            else:
                right = middle - 1
