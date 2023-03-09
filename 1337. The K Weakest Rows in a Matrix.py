from heapq import heappop, heappush, heapify


class Solution:
    def binary_search(self, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == 0:
                if middle == 0 or nums[middle - 1] == 1:
                    return middle

                right = middle - 1
            else:
                left = middle + 1

        return len(nums)

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = [None] * len(mat)
        ans = [None] * k

        for idx, row in enumerate(mat):
            heap[idx] = (self.binary_search(row), idx)

        heapify(heap)

        for idx in range(k):
            ans[idx] = heappop(heap)[1]

        return ans