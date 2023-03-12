class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        first, second = 0, 0
        out = 0

        while first < len(nums1) and second < len(nums2):
            if nums1[first] <= nums2[second]:
                distance = second - first

                if first <= second and distance > out:
                    out = distance

                second += 1
            else:
                first += 1

        return out


class Solution:
    def binary_search_more(self, nums2, target):
        left, right = 0, len(nums2) - 1
        while left <= right:
            middle = (left + right) // 2

            if nums2[middle] == target:
                if middle == len(nums2) - 1 or nums2[middle + 1] != target:
                    return middle

                left = middle + 1

            elif nums2[middle] > target:
                left = middle + 1

            else:
                right = middle - 1

        return right

    def binary_search_less(self, nums1, target):
        left, right = 0, len(nums1) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums1[middle] == target:
                if middle == 0 or nums1[middle - 1] != target:
                    return middle

                right = middle - 1

            elif nums1[middle] > target:
                left = middle + 1

            else:
                right = middle - 1

        return left

    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        out = 0

        if len(nums1) < len(nums2):
            for idx, item in enumerate(nums1):
                binary_search_res = self.binary_search_more(nums2, item)
                if binary_search_res >= idx:
                    out = max(out, binary_search_res - idx)
        else:
            for idx, item in enumerate(nums2):
                binary_search_res = self.binary_search_less(nums1, item)
                if binary_search_res <= idx:
                    out = max(out, idx - binary_search_res)

        return out
    