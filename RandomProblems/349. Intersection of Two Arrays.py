class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # time -- O(nm)
        # space -- O(min(n, m))
        intersection = set()

        for i in range(len(nums1)):
            if nums1[i] not in intersection:
                for j in range(len(nums2)):
                    if nums1[i] == nums2[j]:
                        intersection.add(nums1[i])
                        break

        return list(intersection)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # time -- O((n + m) * log(min(n, m)))
        # space -- O(min(n, m))
        def binary_search(nums, item):
            left, right = 0, len(nums) - 1

            while left <= right:
                middle = (left + right) // 2
                if nums[middle] == item:
                    return True
                elif nums[middle] > item:
                    right = middle - 1
                else:
                    left = middle + 1

        def get_result(nums1, nums2):
            intersection = set()
            nums2.sort()

            for item in nums1:
                if binary_search(nums2, item) is True:
                    intersection.add(item)

            return list(intersection)

        return get_result(nums2, nums1) if len(nums1) > len(nums2) else get_result(nums1, nums2)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # time -- O(n + m)
        # space -- O(n + m)
        def get_intersection(set1, set2):
            return [item for item in set1 if item in set2]

        set1 = set(nums1)
        set2 = set(nums2)

        return get_intersection(set2, set1) if len(set1) > len(set2) else get_intersection(set1, set2)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))

